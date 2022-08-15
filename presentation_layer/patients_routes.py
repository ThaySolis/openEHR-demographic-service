from flask import Blueprint, request, Response
import json

from authentication import auth
from business_layer import patients_controller
from business_layer import exceptions as controller_exceptions
from business_layer.timing import timed, CREATE_PATIENT_MEASUREMENT, UPDATE_PATIENT_MEASUREMENT, DELETE_PATIENT_MEASUREMENT, GET_PATIENT_MEASUREMENT, GET_VERSIONED_PATIENT_MEASUREMENT, GET_VERSIONED_PATIENT_REVISION_HISTORY_MEASUREMENT, GET_VERSIONED_PATIENT_VERSION_MEASUREMENT, LIST_PATIENTS_MEASUREMENT, GET_EHR_ID_FROM_PATIENT_MEASUREMENT, SET_EHR_ID_FROM_PATIENT_MEASUREMENT, GET_CONTRIBUTION_MEASUREMENT

blueprint = Blueprint("patients routes", __name__)

@blueprint.route("/patient", methods=["POST"])
@timed.measure(CREATE_PATIENT_MEASUREMENT)
@auth.login_required
def create_patient():
    if not request.is_json:
        return Response(status = 400, response=None)
    patient_data = request.json
    committer_name = request.authorization.username
    try:
        patient_id = patients_controller.create_patient(patient_data, committer_name)
    except (controller_exceptions.IllegalIdentifierException, controller_exceptions.NotAPersonException):
        return Response(status = 400, response = None)
    except controller_exceptions.NotAuthorizedException:
        return Response(status = 401, response = None)
    except controller_exceptions.NotAPatientException:
        return Response(status = 422, response = None)
    return Response(status = 201, response = None, headers={"Etag":patient_id})

@blueprint.route("/patient/<versioned_object_uid>", methods=["PUT"])
@timed.measure(UPDATE_PATIENT_MEASUREMENT)
@auth.login_required
def update_patient(versioned_object_uid):
    if not request.is_json:
        return Response(status = 400, response = None)
    patient_data = request.json
    if "If-Match" not in request.headers:
        return Response(status = 400, response = None)
    version_id = request.headers["If-Match"]
    patient_id = versioned_object_uid
    committer_name = request.authorization.username
    try:
        new_version_id = patients_controller.update_patient(patient_id, patient_data, version_id, committer_name)
    except (controller_exceptions.IllegalIdentifierException, controller_exceptions.NotAPersonException):
        return Response(status = 400, response = None)
    except controller_exceptions.NotAuthorizedException:
        return Response(status = 401, response = None)
    except (controller_exceptions.NonexistentVersionException, controller_exceptions.PatientAlreadyDeletedException):
        return Response(status = 404, response = None)
    except controller_exceptions.NotTheLatestVersionException as e:
        return Response(status = 412, response = None, headers={"Etag":e.latest_version})
    except controller_exceptions.NotAPatientException:
        return Response(status = 422, response = None)
    return Response(status = 200, response = None, headers={"Etag":new_version_id})

@blueprint.route("/patient/<preceding_version_uid>", methods=["DELETE"])
@timed.measure(DELETE_PATIENT_MEASUREMENT)
@auth.login_required
def delete_patient(preceding_version_uid):
    committer_name = request.authorization.username
    try:
        patients_controller.delete_patient(preceding_version_uid, committer_name)
    except (controller_exceptions.IllegalIdentifierException, controller_exceptions.PatientAlreadyDeletedException):
        return Response(status = 400, response = None)
    except controller_exceptions.NotAuthorizedException:
        return Response(status = 401, response = None)
    except controller_exceptions.NonexistentPatientException:
        return Response(status = 404, response = None)
    except controller_exceptions.NotTheLatestVersionException as e:
        return Response(status = 409, response = None, headers={"Etag":e.latest_version})
    return Response(status = 204, response = None)

@blueprint.route("/patient/<version_or_patient_id>", methods=["GET"])
@timed.measure(GET_PATIENT_MEASUREMENT)
@auth.login_required
def get_patient(version_or_patient_id):
    try:
        patient_data = patients_controller.get_patient(version_or_patient_id, request.args.get("version_at_time"))
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentVersionException, controller_exceptions.NonexistentPatientException, controller_exceptions.NonexistentVersionAtTimeException):
        return Response(status = 404, response = None)
    except controller_exceptions.PatientAlreadyDeletedException:
        return Response(status = 204, response = None)
    return Response(
        status = 200,
        # response = patient_data
        response=json.dumps(patient_data),
        mimetype="application/json"
    )

@blueprint.route("/versioned_patient/<versioned_object_uid>", methods=["GET"])
@timed.measure(GET_VERSIONED_PATIENT_MEASUREMENT)
@auth.login_required
def get_versioned_patient(versioned_object_uid):
    try:
        versioned_party = patients_controller.get_versioned_patient(versioned_object_uid)
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.PatientAlreadyDeletedException):
        return Response(status = 404, response = None)
    return Response(
        status = 200,
        response = json.dumps(versioned_party),
        mimetype="application/json"
    )

@blueprint.route("/versioned_patient/<versioned_object_id>/revision_history", methods=["GET"])
@timed.measure(GET_VERSIONED_PATIENT_REVISION_HISTORY_MEASUREMENT)
@auth.login_required
def get_versioned_patient_revision_history(versioned_object_id):
    try:
        revision_history = patients_controller.get_versioned_patient_revision_history(versioned_object_id)
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.PatientAlreadyDeletedException):
        return Response(status = 404, response = None)
    return Response(
        status = 200,
        response=json.dumps(revision_history),
        mimetype="application/json"
    )
@blueprint.route("/versioned_patient/<versioned_object_uid>/version/<version_uid>", methods=["GET"])
@timed.measure(GET_VERSIONED_PATIENT_VERSION_MEASUREMENT)
@auth.login_required
def get_versioned_patient_version_by_id(versioned_object_uid, version_uid):
    try:
        version_party = patients_controller.get_versioned_patient_version_by_id(versioned_object_uid, version_uid)
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.PatientAlreadyDeletedException, controller_exceptions.NonexistentVersionException):
        return Response(status = 404, response = None)
    return Response(
        status = 200,
        response=json.dumps(version_party),
        mimetype="application/json"
    )

@blueprint.route("/versioned_patient/<versioned_object_id>/version", methods=["GET"])
@timed.measure(GET_VERSIONED_PATIENT_VERSION_MEASUREMENT)
@auth.login_required
def get_versioned_patient_version_at_time(versioned_object_id):
    try:
        version_party = patients_controller.get_versioned_patient_version_at_time(versioned_object_id, request.args.get("version_at_time"))
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.PatientAlreadyDeletedException, controller_exceptions.NonexistentVersionException, controller_exceptions.NonexistentVersionAtTimeException):
        return Response(status = 404, response = None)
    return Response(
        status = 200,
        response=json.dumps(version_party),
        mimetype="application/json"
    )

@blueprint.route("/patient", methods=["GET"])
@timed.measure(LIST_PATIENTS_MEASUREMENT)
@auth.login_required
def list_patients():
    patients_ids = patients_controller.list_patients()
    return Response(
        status = 200,
        response=json.dumps(patients_ids),
        mimetype="application/json"
    )

@blueprint.route("/versioned_patient/<versioned_object_id>/ehr", methods=["GET"])
@timed.measure(GET_EHR_ID_FROM_PATIENT_MEASUREMENT)
@auth.login_required
def get_ehr_id_from_patient(versioned_object_id):
    try:
        patient_to_ehr_association = patients_controller.get_ehr_id_from_patient(versioned_object_id)
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.PatientAlreadyDeletedException):
        return Response(status = 404, response = None)
    return Response(
        status = 200,
        response=json.dumps(patient_to_ehr_association),
        mimetype="application/json"
    )

@blueprint.route("/versioned_patient/<versioned_object_id>/ehr", methods=["PUT"])
@timed.measure(SET_EHR_ID_FROM_PATIENT_MEASUREMENT)
@auth.login_required
def set_ehr_id_of_patient(versioned_object_id):
    patient_to_ehr_association = request.json
    try:
        patients_controller.set_ehr_id_of_patient(versioned_object_id, patient_to_ehr_association)
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.PatientAlreadyDeletedException):
        return Response(status = 404, response = None)
    return Response(
        status = 201,
        response= None
    )

@blueprint.route("/versioned_patient/<versioned_patient_id>/contribution/<contribution_id>", methods=["GET"])
@timed.measure(GET_CONTRIBUTION_MEASUREMENT)
@auth.login_required
def get_contribution(versioned_patient_id, contribution_id):
    try:
        contribution = patients_controller.get_contribution(versioned_patient_id, contribution_id)
    except controller_exceptions.IllegalIdentifierException:
        return Response(status = 400, response = None)
    except (controller_exceptions.NonexistentPatientException, controller_exceptions.NonexistentContributionException):
        return Response(status = 404, response = None)
    return Response(
        status = 200,
        response=json.dumps(contribution),
        mimetype="application/json"
    )
