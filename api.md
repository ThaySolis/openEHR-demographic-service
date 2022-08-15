# openEHR demographic service API

This document contains a description of the API of the openEHR demographic API service.

## Create patient

This API call creates a new versioned patient (`VERSIONED_PARTY`) and its first version.

- **Request**:
    - **Method**: `POST`
    - **Path**: `/patient`
    - **Payload**: a JSON document with the `PERSON` object.
- **Response**:
    - `201 Created` is returned when the patient was created.
        - **Payload**: empty
        - **Headers**:
            - `Etag`: the ID of the first version.
    - `400 Bad Request` is returned when the request has
    invalid content (content could not be converted to a valid `PERSON`).
        - **Payload**: empty
    - `422 Unprocessable Entity` is returned when the content could be converted to a `PERSON`, but it does not conform to the `openEHR-DEMOGRAPHIC-PERSON.person-patient.v0` archetype.
        - **Payload**: empty

## Update patient

This API call updates the data of a patient identified by `versioned_object_uid`. If the request body already contains a `PERSON.uid.value`, it must match the `versioned_object_uid` in the URL. The existing latest `version_uid` of the `PERSON` resource (i.e the `preceding_version_uid`) must be specified in the `If-Match` header.

- **Request**:
    - **Method**: `PUT`
    - **Path**: `/patient/<versioned_object_uid>`
    - **Path parameters**:
        - `versioned_object_uid`: identifier of the patient to be updated.
    - **Headers**:
        - `If-Match`: identifier of the latest version of the patient to be updated.
    - **Payload**: a JSON document with the `PERSON` object.
- **Response**:
    - `200 OK` is returned when the patient (`PERSON`) is successfully updated
        - **Payload**: empty
        - **Headers**:
            - `Etag`: the ID of the new patient version.
    - `400 Bad Request` is returned when the request has
    invalid content (content could not be converted to a valid `PERSON`).
        - **Payload**: empty
    - `404 Not Found` is returned when a patient with `versioned_object_uid` does not exist or when they were deleted.
    - `412 Precondition Failed` is returned when `If-Match` request header doesn’t match the latest version (of this versioned object) on the service side.
        - **Payload**: empty
        - **Headers**:
            - `Etag`: the ID of the latest patient version.
    - `422 Unprocessable Entity` is returned when the content could be converted to a `PERSON`, but it does not conform to the `openEHR-DEMOGRAPHIC-PERSON.person-patient.v0` archetype.
        - **Payload**: empty

## Delete patient

This API call deletes the patient identified by `preceding_version_uid`.

- **Request**:
    - **Method**: `DELETE`
    - **Path**: `/patient/<preceding_version_uid>`
    - **Path parameters**:
        - `preceding_version_uid`: identifier of the patient to be deleted. This MUST be the last (most recent) version.
- **Response**:
    - `204 No Content` is returned when the patient was deleted.
        - **Payload**: empty
    - `400 Bad Request` is returned when the patient with `preceding_version_uid` is already deleted.
        - **Payload**: empty
    - `404 Not Found` is returned when a patient with `preceding_version_uid` does not exist.
        - **Payload**: empty
    - `409 Conflict` is returned when supplied `preceding_version_uid` doesn’t match the latest version.
        - **Payload**: empty
        - **Headers**:
            - `Etag`: the ID of the latest patient version.

## Get patient by version ID

This API call retrieves particular version of the patient identified by `version_uid`

- **Request**:
    - **Method**: `GET`
    - **Path**: `/patient/<version_uid>`
    - **Path parameters**:
        - `version_uid`: ID of the patient version, taken from `VERSION<PARTY>.uid.value`
- **Response**:
    - `200 OK` is returned when the patient is successfully retrieved.
        - **Payload**: a JSON document with the `PERSON` object.
    - `204 No Content` is returned when the patient is deleted (logically).
        - **Payload**: empty.
    - `404 Not Found` is returned when a patient with `version_uid` does not exist
        - **Payload**: empty.

## Get patient at time

This API call retrieves a version of the patient identified by `versioned_object_uid`. If `version_at_time` is supplied, retrieves the version extant at specified time, otherwise retrieves the latest patient version.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/patient/<versioned_object_uid>[?<version_at_time>]`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
        - `version_at_time`: A given time in the extended ISO 8601 format (RFC 3339)
- **Response**:
    - `200 OK` is returned when the patient is successfully retrieved.
        - **Payload**: a JSON document with the `PERSON` object.
    - `204 No Content` is returned when the patient with `versioned_object_uid` at specified `version_at_time` time has been deleted.
        - **Payload**: empty.
    - `404 Not Found` is returned when a `VERSIONED_PARTY` with `versioned_object_uid` does not exist or when a patient does not exists at `version_at_time` time.
        - **Payload**: empty.

## Get versioned patient

This API call retrieves a `VERSIONED_PARTY` identified by `versioned_object_uid`

- **Request**:
    - **Method**: `GET`
    - **Path**: `/versioned_patient/<versioned_object_uid>`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
- **Response**:
    - `200 OK` is returned when the `VERSIONED_PARTY` is successfully retrieved.
        - **Payload**: a JSON document with the `PERSON` object.
    - `404 Not Found` is returned when a `VERSIONED_PARTY` with `versioned_object_uid` does not exist.
        - **Payload**: empty.

## Get versioned patient revision history

This API call retrieves the revision history of the `VERSIONED_PARTY` identified by `versioned_object_uid`.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/versioned_patient/<versioned_object_uid>/revision_history`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
- **Response**:
    - `200 OK` is returned when the `VERSIONED_PARTY` revision history is successfully retrieved.
        - **Payload**: a JSON document with the `REVISION_HISTORY` of the `VERSIONED_PARTY` object.
    - `404 Not Found` is returned when a `VERSIONED_PARTY` with `versioned_object_uid` does not exist.
        - **Payload**: empty.

## Get versioned patient version by id

This API call retrieves a `VERSION` identified by `version_uid` of a `VERSIONED_PARTY` identified by `versioned_object_uid`.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/versioned_patient/<versioned_object_uid>/version/<version_uid>`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
        - `version_uid`: ID of the patient version, taken from `VERSION<PARTY>.uid.value`
- **Response**:
    - `200 OK` is returned when the `VERSION` is successfully retrieved.
        - **Payload**: a JSON document with the `VERSION<PARTY>` object.
    - `404 Not Found` is returned when a `VERSIONED_PARTY` with `versioned_object_uid` does not exist or when a `VERSION` with `version_uid` does not exist.
        - **Payload**: empty.

## Get versioned patient version at time

This API call retrieves a `VERSION` from the `VERSIONED_PARTY` identified by `versioned_object_uid`. If `version_at_time` is supplied, retrieves the `VERSION` extant at specified time, otherwise retrieves the latest `VERSION`.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/versioned_patient/<versioned_object_uid>/version[?<version_at_time>]`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
        - `version_at_time`: A given time in the extended ISO 8601 format (RFC 3339)
- **Response**:
    - `200 OK` is returned when the `VERSION` is successfully retrieved.
        - **Payload**: a JSON document with the `VERSION<PARTY>` object.
    - `404 Not Found` when a `VERSIONED_PARTY` with `versioned_object_uid` does not exist or when a `VERSION` with `version_uid` does not exist.
        - **Payload**: empty.

## List patients

This API call lists the IDs of all the patients in the system.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/patient`
- **Response**:
    - `200 OK`, on success.
        - **Payload**: a list where each element is a patient's ID.


## Get EHR id from patient

This API call retrieves the EHR identifier associated with a given patient.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/versioned_patient/<versioned_object_uid>/ehr`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
- **Response**:
    - `200 OK` is returned when the patient exists.
        - **Payload**: a JSON document with a single attribute: `ehr_uid`. Tf the patient is associated with an EHR, the field is not `null` and its value is a `HIER_OBJECT_ID`.
    - `404 Not Found` when the patient does not exist or was already deleted.
        - **Payload**: empty.

## Set EHR id of patient

This API call sets the EHR identifier associated with a given patient.

- **Request**:
    - **Method**: `PUT`
    - **Path**: `/versioned_patient/<versioned_object_uid>/ehr`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
    - **Payload**: a JSON document with a single attribute: `ehr_uid`, which may either be `null` or a `HIER_OBJECT_ID`.
- **Response**:
    - `200 OK` is returned when the EHR identifier has been set.
        - **Payload**: empty.
    - `404 Not Found` when the patient does not exist or was already deleted.
        - **Payload**: empty.

## Get contribution

This API call retrieves a contribution of a given patient.

- **Request**:
    - **Method**: `GET`
    - **Path**: `/versioned_patient/{versioned_patient_id}/contribution/{contribution_uid}`
    - **Path parameters**:
        - `versioned_object_uid`: ID of the versioned patient, taken from `VERSIONED_PARTY.uid.value`
        - `contribution_uid`: ID of the contribution, taken from `VERSION<PARTY>.contribution.uid.value`
- **Response**:
    - `200 OK` is returned when the contribution was retrieved.
        - **Payload**: a JSON document with the `CONTRIBUTION`.
    - `404 Not Found` when the patient does not exist or the contribution does not exist.
        - **Payload**: empty.
