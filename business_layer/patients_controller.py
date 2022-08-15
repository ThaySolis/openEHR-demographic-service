from data_layer.rm_validation import validate_PERSON
from data_layer.archetype_validation import validate_archetype_DEMOGRAPHIC_PERSON_person_patient_v0 as validate_patient
from data_layer.rm_generation import generate_instance_of_HIER_OBJECT_ID, generate_instance_of_OBJECT_VERSION_ID, generate_instance_of_VERSIONED_PARTY, generate_instance_of_REVISION_HISTORY_ITEM, generate_instance_of_REVISION_HISTORY, generate_instance_of_ORIGINAL_VERSION, generate_instance_of_CONTRIBUTION_representing_creation, generate_instance_of_CONTRIBUTION_representing_modification, generate_instance_of_CONTRIBUTION_representing_deletion
from data_layer.time import time_now
from data_layer import repository, ids

import business_layer.exceptions as controller_exceptions

def create_patient(patient_data : dict, committer_name : str) -> str:
    '''
    Creates a new patient in database

    Parameters:
        patient_data - patient's data
        committer_name - the username responsible for the action

    Returns:
        The ID of the first version of the inserted patient, in case of success
        None in case of fail
    '''

    time_of_operation = time_now()

    #Validates input data.
    if committer_name is None or not isinstance(committer_name, str) or committer_name == "":
        raise controller_exceptions.NotAuthorizedException(f"The committer was not provided!")
    if not validate_PERSON(patient_data):
        raise controller_exceptions.NotAPersonException("The provided data is not a PERSON!")
    if not validate_patient(patient_data):
        raise controller_exceptions.NotAPatientException("The provided data is not a patient!")

    #Checks if received PERSON already has an identifier.
    patient_id_from_data = None
    if "uid" in patient_data:
        #Tries to get a patient identifier from the provided value.
        id = patient_data["uid"]["value"]
        if id is None or id == "":
            raise controller_exceptions.IllegalIdentifierException(f"The patient or version id was not provided.")
        elif ids.is_version_id(id):
            patient_id_from_data = ids.extract_versioned_object_id_from_version_id(id)
        elif ids.is_versioned_object_id(id):
            patient_id_from_data = id
        else:
            raise controller_exceptions.IllegalIdentifierException(f"The provided id '{id}' is neither a valid patient id nor a valid version id!")

        #Removes the identifier from the PERSON data.
        patient_data.pop("uid")

    #Generates IDs.
    if patient_id_from_data is not None:
        patient_id = patient_id_from_data
    else:
        patient_id = ids.generate_versioned_object_id()
    first_version_id = ids.generate_first_version_id(patient_id)
    contribution_id = ids.generate_versioned_object_id()

    #Generates the CONTRIBUTION.
    contribution = generate_instance_of_CONTRIBUTION_representing_creation(contribution_id, first_version_id, "PERSON", committer_name, time_of_operation)

    with repository.begin_transaction() as transaction:
        #Inserts documents.
        succeeded = repository.insert_patient_document(patient_id, first_version_id, contribution_id, patient_data, time_of_operation, transaction = transaction)
        if succeeded:
            repository.insert_contribution_document(contribution_id, contribution, transaction = transaction)
        else:
            raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' belongs to another patient!")

        #Returns the ID of the first version.
        return first_version_id

def update_patient(patient_id : str, patient_data : dict, previous_version_id : str, committer_name : str) -> str:
    '''
    Updates the data of a specific patient

    Parameters:
        patient_id - the id of the patient which information will be updated
        patient_data - the new patient's data that will be updated
        previous_version_id - the id of the last version of the patient
        committer_name - the username responsible for the action

    Returns:
        The next version ID
    '''

    time_of_operation = time_now()

    #Validates input data.
    if committer_name is None or not isinstance(committer_name, str) or committer_name == "":
        raise controller_exceptions.NotAuthorizedException(f"The committer was not provided!")
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")
    if previous_version_id is None or previous_version_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The version id was not provided.")
    if not ids.is_version_id(previous_version_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided version id '{previous_version_id}' is not valid!")
    if not validate_PERSON(patient_data):
        raise controller_exceptions.NotAPersonException("The provided data is not a PERSON!")
    if not validate_patient(patient_data):
        raise controller_exceptions.NotAPatientException("The provided data is not a patient!")

    #Checks if received PERSON already has an identifier.
    patient_id_from_data = None
    if "uid" in patient_data:
        #Tries to get a patient identifier from the provided value.
        id = patient_data["uid"]["value"]
        if id is None or id == "":
            raise controller_exceptions.IllegalIdentifierException(f"The patient or version id was not provided.")
        elif ids.is_version_id(id):
            patient_id_from_data = ids.extract_versioned_object_id_from_version_id(id)
        elif ids.is_versioned_object_id(id):
            patient_id_from_data = id
        else:
            raise controller_exceptions.IllegalIdentifierException(f"The provided id '{id}' is neither a valid patient id nor a valid version id!")

        #Removes the identifier from the PERSON data.
        patient_data.pop("uid")

    # Validates parameters for consistency
    if patient_id_from_data is not None and patient_id_from_data != patient_id:
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id is {patient_id}, but the patient data belong to patient {patient_id_from_data}!")

    with repository.begin_transaction() as transaction:
        #Retrieves the patient document from the database.
        patient_document = repository.find_patient_document(patient_id, transaction = transaction)
        if patient_document is None:
            raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

        #Aborts if the patient has been deleted.
        if repository.is_deleted_in_patient_document(patient_document):
            raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

        #Aborts if the wrong version ID has been provided.
        latest_version_id = repository.get_most_recent_version_id_from_patient_document(patient_document)
        if latest_version_id != previous_version_id:
            raise controller_exceptions.NotTheLatestVersionException(f"Version {previous_version_id} is not the latest version!", latest_version_id)

        #Generates IDs.
        next_version_id = ids.generate_next_version_id(previous_version_id)
        contribution_id = ids.generate_versioned_object_id()

        #Generates the CONTRIBUTION.
        contribution = generate_instance_of_CONTRIBUTION_representing_modification(contribution_id, next_version_id, "PERSON", committer_name, time_of_operation)

        #Inserts and updates documents.
        repository.insert_contribution_document(contribution_id, contribution, transaction = transaction)
        repository.add_version_to_patient_document(patient_id, next_version_id, contribution_id, patient_data, time_of_operation, transaction = transaction)

        #Returns the ID of the generated version.
        return next_version_id


def delete_patient(previous_version_id : str, committer_name : str) -> None:
    '''
    Deletes the last version of the patient with given ID

    Parameters:
        previous_version_id - the id of the last version of the patient
        committer_name - the username responsible for the actions
    '''

    time_of_operation = time_now()

    #Validates input data.
    if committer_name is None or not isinstance(committer_name, str) or committer_name == "":
        raise controller_exceptions.NotAuthorizedException(f"The committer was not provided!")
    if previous_version_id is None or previous_version_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The version id was not provided.")
    if not ids.is_version_id(previous_version_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided version id '{previous_version_id}' is not valid!")

    #Extracts the patient ID from the version ID.
    patient_id = ids.extract_versioned_object_id_from_version_id(previous_version_id)

    with repository.begin_transaction() as transaction:
        #Retrieves the patient document from the database.
        patient_document = repository.find_patient_document(patient_id, transaction = transaction)
        if patient_document is None:
            raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

        #Aborts if the patient has been deleted.
        if repository.is_deleted_in_patient_document(patient_document):
            raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

        #Aborts if the wrong version ID has been provided.
        latest_version_id = repository.get_most_recent_version_id_from_patient_document(patient_document)
        if latest_version_id != previous_version_id:
            raise controller_exceptions.NotTheLatestVersionException(f"Version {previous_version_id} is not the latest version!", latest_version_id)

        #Generates ID.
        contribution_id = ids.generate_versioned_object_id()

        #Generates the CONTRIBUTION.
        contribution = generate_instance_of_CONTRIBUTION_representing_deletion(contribution_id, committer_name, time_of_operation)

        #Inserts and updates documents.
        repository.insert_contribution_document(contribution_id, contribution, transaction = transaction)
        repository.set_deleted_in_patient_document(patient_id, True, transaction = transaction)

def get_patient(id : str, time : str = None) -> dict:
    '''
    Reads a patient's data by patient_id ou version_id

    Parameters:
        id - version_id (the id of a specific version of the patient) or versioned object id (the id of the patient - latest version)
        time (optional) - date + hour

    Returns:
        The corresponding function
    '''
    if id is None or id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient or version id was not provided.")
    elif ids.is_version_id(id):
        return get_patient_by_version(id)
    elif ids.is_versioned_object_id(id):
        return get_patient_by_versioned_object_id(id, time)
    else:
        raise controller_exceptions.IllegalIdentifierException(f"The provided id '{id}' is neither a valid patient id nor a valid version id!")

def get_patient_by_version(version_id : str) -> dict:
    '''
    Reads a patient's data by version_id

    Parameters:
        version_id - version_id (the id of a specific version of the patient)

    Returns:
        The corresponding data
    '''

    #Validates input data.
    if version_id is None or version_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The version id was not provided.")
    if not ids.is_version_id(version_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided version id '{version_id}' is not valid!")

    #Extracts the patient ID from the version ID.
    patient_id = ids.extract_versioned_object_id_from_version_id(version_id)

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    #Looks for the version ID in the document.
    (_, _, _, _, patient_data) = repository.find_version_in_patient_document(patient_document, version_id)

    #Aborts if no version found.
    if patient_data is None:
        raise controller_exceptions.NonexistentVersionException(f"The patient with id {patient_id} does not have a version with id {version_id}")

    #Adds an idenitifier to the PERSON instance.
    patient_data["uid"] = generate_instance_of_OBJECT_VERSION_ID(version_id, include_type_definition = True)

    #Returns the PERSON (patient) instance.
    return patient_data

def get_patient_by_versioned_object_id(patient_id : str, time : str = None) -> dict:
    '''
    Reads a patient's data by patient_id. If time is provided, it returns the version at the corresponding time.
    If not, it returns the latest version of the patient_id.

    Parameters:
        patient_id - the ID of the patient
        time - date/time

    Returns:
        The data of the patient version at the corresponding time or the latest version of the patient.
    '''

    #TODO: validar data/hora fornecidas

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    #Finds the version ID based on the time.
    if time is None:
        version_id = repository.get_most_recent_version_id_from_patient_document(patient_document)
    else:
        version_id = repository.find_version_id_by_time_in_patient_document(patient_document, time)

    #Looks for the version ID in the document.
    patient_data = None
    if version_id is not None:
        (_, _, _, _, patient_data) = repository.find_version_in_patient_document(patient_document, version_id)

    #Aborts if no version found.
    if patient_data is None:
        raise controller_exceptions.NonexistentVersionAtTimeException(f"There is no version of the patient {patient_id} at the given time.")

    #Adds an idenitifier to the PERSON instance.
    patient_data["uid"] = generate_instance_of_OBJECT_VERSION_ID(version_id, include_type_definition = True)

    #Returns the PERSON (patient) instance.
    return patient_data

def get_versioned_patient(patient_id : str) -> dict:
    #TODO: adicionar documentação

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    #Gets the creation time of the first version.
    first_version_id = repository.get_first_version_id_from_patient_document(patient_document)
    (_, _, time_created, _, _) = repository.find_version_in_patient_document(patient_document, first_version_id)

    #Generates and returns the VERSIONED_PARTY instance.
    versioned_party = generate_instance_of_VERSIONED_PARTY(patient_id, time_created)
    return versioned_party

def get_versioned_patient_revision_history(patient_id : str) -> dict:
    #TODO: adicionar documentação

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    #TODO: mover para o repository.
    revision_history_items = []
    for version in patient_document["versions"]:
        contribution_id = version["contribution_id"]

        #Retrieves the contribution document from the database.
        contribution_document = repository.find_contribution_document(contribution_id)

        #Extracts the AUDIT_DETAILS from the CONTRIBUTION.
        audit_details = None
        if contribution_document is not None:
            contribution = repository.extract_contribution_from_contribution_document(contribution_document)
            audit_details = contribution["audit"]

        #Generates and appends the REVISION_HISTORY_ITEM instance.
        revision_history_item = generate_instance_of_REVISION_HISTORY_ITEM(version["uid"], [ audit_details ])
        revision_history_items.append(revision_history_item)

    #Generates and returns the REVISION_HISTORY instance.
    revision_history = generate_instance_of_REVISION_HISTORY(revision_history_items)
    return revision_history

def get_versioned_patient_version_by_id(patient_id : str, version_id : str) -> dict:
    #TODO: adicionar documentação

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")
    if version_id is None or version_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The version id was not provided.")
    if not ids.is_version_id(version_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided version id '{version_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    #Looks for the version ID in the document.
    (found_version_id, preceding_version_id, _, contribution_id, _) = repository.find_version_in_patient_document(patient_document, version_id)

    #Aborts if no version found.
    if found_version_id is None:
        raise controller_exceptions.NonexistentVersionException(f"The patient with id {patient_id} does not have a version with id {version_id}")

    #Retrieves the contribution document from the database.
    contribution_document = repository.find_contribution_document(contribution_id)

    #Extracts the AUDIT_DETAILS from the CONTRIBUTION.
    audit_details = None
    if contribution_document is not None:
        contribution = repository.extract_contribution_from_contribution_document(contribution_document)
        audit_details = contribution["audit"]

    #Generates and returns the ORIGINAL_VERSION instance.
    original_version = generate_instance_of_ORIGINAL_VERSION(
        version_id,
        preceding_version_id,
        contribution_id,
        audit_details,
        include_type_definition = True
    )
    return original_version

def get_versioned_patient_version_at_time(patient_id : str, time : str = None) -> dict:
    #TODO: adicionar documentação
    #TODO: validar data/hora fornecidas

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    #Finds the version ID based on the time.
    if time is None:
        version_id = repository.get_most_recent_version_id_from_patient_document(patient_document)
    else:
        version_id = repository.find_version_id_by_time_in_patient_document(patient_document, time)

    #Looks for the version ID in the document.
    found_version_id = None
    if version_id is not None:
        (found_version_id, preceding_version_id, _, contribution_id, _) = repository.find_version_in_patient_document(patient_document, version_id)

    #Aborts if no version found.
    if found_version_id is None:
        raise controller_exceptions.NonexistentVersionAtTimeException(f"There is no version of the patient {patient_id} at the given time.")

    #Retrieves the contribution document from the database.
    contribution_document = repository.find_contribution_document(contribution_id)

    #Extracts the AUDIT_DETAILS from the CONTRIBUTION.
    audit_details = None
    if contribution_document is not None:
        contribution = repository.extract_contribution_from_contribution_document(contribution_document)
        audit_details = contribution["audit"]

    #Generates and returns the ORIGINAL_VERSION instance.
    original_version = generate_instance_of_ORIGINAL_VERSION(
        version_id,
        preceding_version_id,
        contribution_id,
        audit_details,
        include_type_definition = True
    )
    return original_version

def list_patients() -> dict:
    #TODO: adicionar documentação

    patient_ids = repository.find_all_patient_ids()
    return {
        "uids": [generate_instance_of_HIER_OBJECT_ID(patient_id) for patient_id in patient_ids]
    }

def get_ehr_id_from_patient(patient_id : str) -> dict:
    #TODO: adicionar documentação

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Aborts if the patient has been deleted.
    if repository.is_deleted_in_patient_document(patient_document):
        raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

    patient_to_ehr_association = {}

    ehr_id = repository.get_ehr_id_from_patient_document(patient_document)
    if ehr_id is not None:
        patient_to_ehr_association["ehr_uid"] = generate_instance_of_HIER_OBJECT_ID(ehr_id)

    return patient_to_ehr_association

def set_ehr_id_of_patient(patient_id : str, patient_to_ehr_association : str) -> None:
    #TODO: adicionar documentação

    #Extracts the EHR ID from the association.
    ehr_id = None
    if "ehr_uid" in patient_to_ehr_association:
        if "value" in patient_to_ehr_association["ehr_uid"]:
            ehr_id = patient_to_ehr_association["ehr_uid"]["value"]

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")
    if ehr_id is not None and not ids.is_versioned_object_id(ehr_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided ehr id '{ehr_id}' is not valid!")

    with repository.begin_transaction() as transaction:
        #Retrieves the patient document from the database.
        patient_document = repository.find_patient_document(patient_id, transaction = transaction)
        if patient_document is None:
            raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

        #Aborts if the patient has been deleted.
        if repository.is_deleted_in_patient_document(patient_document):
            raise controller_exceptions.PatientAlreadyDeletedException(f"The patient with id {patient_id} was already deleted!")

        #Updates the EHR ID.
        repository.set_ehr_id_of_patient_document(patient_id, ehr_id, transaction = transaction)

def get_contribution(patient_id : str, contribution_id : str) -> dict:
    #TODO: adicionar documentação

    #Validates input data.
    if patient_id is None or patient_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The patient id was not provided.")
    if not ids.is_versioned_object_id(patient_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided patient id '{patient_id}' is not valid!")
    if contribution_id is None or contribution_id == "":
        raise controller_exceptions.IllegalIdentifierException(f"The contribution id was not provided.")
    if not ids.is_versioned_object_id(contribution_id):
        raise controller_exceptions.IllegalIdentifierException(f"The provided contribution id '{patient_id}' is not valid!")

    #Retrieves the patient document from the database.
    patient_document = repository.find_patient_document(patient_id)
    if patient_document is None:
        raise controller_exceptions.NonexistentPatientException(f"There is no patient with id {patient_id}!")

    #Retrieves the contribution document from the database.
    contribution_document = repository.find_contribution_document(contribution_id)
    if contribution_document is None:
        raise controller_exceptions.NonexistentContributionException(f"There is no contribution with id {contribution_id}!")

    # TODO verificar se a CONTRIBUTION pertence ao paciente em questão.

    #Extracts the CONTRIBUTION from the document.
    contribution = repository.extract_contribution_from_contribution_document(contribution_document)
    return contribution
