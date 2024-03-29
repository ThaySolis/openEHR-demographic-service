from uuid import uuid4, UUID

from app_settings import SYSTEM_ID

def generate_guid() -> str:
    """
    Generates a new globally unique identifier (GUID).
    """

    # https://specifications.openehr.org/releases/BASE/Release-1.0.2/architecture_overview.html#_identification_of_the_ehr

    return str(uuid4())

def generate_versioned_object_id() -> str:
    """
    Generates an identifier for a versioned object.
    """

    return generate_guid()

def generate_next_version_id(previous_version_id : str) -> str:
    """
    Generates a new version identifier based on the identifier of the previous one.
    """

    # https://specifications.openehr.org/releases/BASE/latest/base_types.html#_identifying_versions_within_openehr_versioned_containers

    version_id_parts = previous_version_id.split("::")

    versioned_object_id = version_id_parts[0]
    previous_version_number = int(version_id_parts[2])

    next_version_number = previous_version_number + 1

    return f"{versioned_object_id}::{SYSTEM_ID}::{next_version_number}"

def generate_first_version_id(versioned_object_id):
    """
    Generates the identifier of the first version of an identified object.
    """

    return f"{versioned_object_id}::{SYSTEM_ID}::1"

def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid("c9bf9e57-1685-4c89-bafb-ff5af830be8a")
    True
    >>> is_valid_uuid("c9bf9e58")
    False
    """
    # Taken from https://stackoverflow.com/a/33245493
    try:
        UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return True

def is_version_id(id):
    """
    Checks if the provided value is a valid version identifier.
    """

    version_id_parts = id.split("::")
    if id is not None and isinstance(id, str):
        if len(version_id_parts) == 3:
            if is_valid_uuid(version_id_parts[0]):
                if version_id_parts[2].isdecimal():
                    return True
    return False

def is_versioned_object_id(id):
    """
    Checks if the provided value is a valid versioned object identifier.
    """

    if id is not None and isinstance(id, str):
        version_id_parts = id.split("::")
        if len(version_id_parts) == 1:
            if is_valid_uuid(version_id_parts[0]):
                return True
    return False

def extract_versioned_object_id_from_version_id(version_id):
    """
    Extracts the versioned object identifier from the identifier of one of its versions.
    """

    version_id_parts = version_id.split("::")

    versioned_object_id = version_id_parts[0]

    return versioned_object_id
