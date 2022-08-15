from datetime import datetime

from app_settings import SYSTEM_ID

def generate_instance_of_HIER_OBJECT_ID(object_id_value : str, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of HIER_OBJECT_ID.
    """

    # documentation: <https://specifications.openehr.org/releases/BASE/latest/base_types.html#_object_id_class>

    instance = {
        "value": object_id_value
    }
    if include_type_definition:
        instance["_type"] = "HIER_OBJECT_ID"
    return instance

def generate_instance_of_OBJECT_VERSION_ID(version_id : str, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of OBJECT_VERSION_ID.
    """

    # documentation: <https://specifications.openehr.org/releases/BASE/latest/base_types.html#_object_id_class>

    instance = {
        "value": version_id
    }
    if include_type_definition:
        instance["_type"] = "OBJECT_VERSION_ID"
    return instance

def generate_instance_of_OBJECT_REF(object_id : dict, rm_type : str, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of OBJECT_REF.
    """

    # documentation: <https://specifications.openehr.org/releases/BASE/latest/base_types.html#_object_ref_class>
    instance = {
        "id": object_id,
        "type": rm_type,
        "namespace": "local"
    }
    if include_type_definition:
        instance["_type"] = "OBJECT_REF"
    return instance

def generate_instance_of_DV_DATE_TIME(value : datetime, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of DV_DATE_TIME.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/latest/data_types.html#_dv_date_time_class>
    instance = {
        "value": value.isoformat()
    }
    if include_type_definition:
        instance["_type"] = "DV_DATE_TIME"
    return instance

def generate_instance_of_DV_CODED_TEXT(value : str, code_string : str, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of DV_CODED_TEXT.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/latest/data_types.html#_dv_coded_text_class>
    instance = {
        "value": value,
        "defining_code": {
            "terminology_id": {
                "value": "openehr"
            },
            "code_string": code_string
        }
    }
    if include_type_definition:
        instance["_type"] = "DV_CODED_TEXT"
    return instance

def generate_instance_of_PARTY_IDENTIFIED(name_value : str, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of PARTY_IDENTIFIED that represents the patient with a given ID.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/latest/common.html#_party_identified_class>
    instance = {
        "name": name_value
    }
    if include_type_definition:
        instance["_type"] = "PARTY_IDENTIFIED"
    return instance

def generate_instance_of_AUDIT_DETAILS(change_type_value : str, change_type_code_string : str, committer_name : str, time_committed : datetime, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of AUDIT_DETAILS that represents the patient with a given ID.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/latest/common.html#_audit_details_class>
    instance = {
        "system_id": SYSTEM_ID,
        "committer": generate_instance_of_PARTY_IDENTIFIED(committer_name, include_type_definition = True),
        "time_committed": generate_instance_of_DV_DATE_TIME(time_committed),
        "change_type": generate_instance_of_DV_CODED_TEXT(change_type_value, change_type_code_string)
    }
    if include_type_definition:
        instance["_type"] = "AUDIT_DETAILS"
    return instance

def generate_instance_of_REVISION_HISTORY_ITEM(version_id : str, audit_details_list : list, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of REVISION_HISTORY_ITEM.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/Release-1.0.3/common.html#_revision_history_item_class>
    instance = {
        "version_id": generate_instance_of_OBJECT_VERSION_ID(version_id),
        "audits": audit_details_list
    }
    if include_type_definition:
        instance["_type"] = "REVISION_HISTORY_ITEM"
    return instance

def generate_instance_of_REVISION_HISTORY(revision_history_items : list, include_type_definition : bool = False) -> dict:
    # documentation: <https://specifications.openehr.org/releases/RM/Release-1.0.3/common.html#_revision_history_class>
    """
    Generates an instance of REVISION_HISTORY.
    """

    instance = {
        "items": revision_history_items
    }
    if include_type_definition:
        instance["_type"] = "REVISION_HISTORY"
    return instance

def generate_instance_of_ORIGINAL_VERSION(version_id : str, preceding_version_id : str, contribution_id : str, audit_details : dict, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of ORIGINAL_VERSION.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/Release-1.0.3/common.html#_original_version_t_class>
    instance = {
        "uid": generate_instance_of_OBJECT_VERSION_ID(version_id),
        "contribution": generate_instance_of_OBJECT_REF(
            generate_instance_of_HIER_OBJECT_ID(contribution_id, include_type_definition = True),
            "CONTRIBUTION"
        ),
        "commit_audit": audit_details,
        "lifecycle_state": generate_instance_of_DV_CODED_TEXT("complete", "532")
    }
    if preceding_version_id is not None:
        instance["preceding_version_id"] = generate_instance_of_OBJECT_VERSION_ID(preceding_version_id)
    if include_type_definition:
        instance["_type"] = "ORIGINAL_VERSION"
    return instance

def generate_instance_of_VERSIONED_PARTY(patient_id : str, time_created : datetime, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of VERSIONED_PARTY that represents the patient with a given ID.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/latest/demographic.html#_versioned_party_class>
    instance = {
        "_type": "VERSIONED_PARTY",
        "uid": generate_instance_of_HIER_OBJECT_ID(patient_id),
        "time_created": generate_instance_of_DV_DATE_TIME(time_created)
    }
    if include_type_definition:
        instance["_type"] = "VERSIONED_PARTY"
    return instance

def generate_instance_of_CONTRIBUTION_representing_creation(contribution_id : str, version_id : str, rm_type : str, committer_name : str, time_committed : datetime, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of CONTRIBUTION that represents the creation of a versioned object.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/Release-1.0.3/common.html#_contribution_class>
    instance = {
        "uid": generate_instance_of_HIER_OBJECT_ID(contribution_id),
        "versions": [
            generate_instance_of_OBJECT_REF(
                generate_instance_of_OBJECT_VERSION_ID(version_id, include_type_definition = True),
                rm_type
            )
        ],
        "audit": generate_instance_of_AUDIT_DETAILS("creation", "249", committer_name, time_committed)
    }
    if include_type_definition:
        instance["_type"] = "CONTRIBUTION"
    return instance

def generate_instance_of_CONTRIBUTION_representing_modification(contribution_id : str, version_id : str, rm_type : str, committer_name : str, time_committed : datetime, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of CONTRIBUTION that represents the modification of a versioned object.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/Release-1.0.3/common.html#_contribution_class>
    instance = {
        "uid": generate_instance_of_HIER_OBJECT_ID(contribution_id),
        "versions": [
            generate_instance_of_OBJECT_REF(
                generate_instance_of_OBJECT_VERSION_ID(version_id, include_type_definition = True),
                rm_type
            )
        ],
        "audit": generate_instance_of_AUDIT_DETAILS("modification", "251", committer_name, time_committed)
    }
    if include_type_definition:
        instance["_type"] = "CONTRIBUTION"
    return instance

def generate_instance_of_CONTRIBUTION_representing_deletion(contribution_id : str, committer_name : str, time_committed : datetime, include_type_definition : bool = False) -> dict:
    """
    Generates an instance of CONTRIBUTION that represents the deletion of a versioned object.
    """

    # documentation: <https://specifications.openehr.org/releases/RM/Release-1.0.3/common.html#_contribution_class>
    instance = {
        "_type": "CONTRIBUTION",
        "uid": generate_instance_of_HIER_OBJECT_ID(contribution_id),
        "versions": [],
        "audit": generate_instance_of_AUDIT_DETAILS("deletion", "523", committer_name, time_committed)
    }
    if include_type_definition:
        instance["_type"] = "CONTRIBUTION"
    return instance
