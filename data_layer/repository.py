from pymongo import MongoClient
from pymongo.client_session import ClientSession
import pymongo.errors as pymongo_errors
from datetime import datetime
from contextlib import contextmanager
from typing import Tuple

from data_layer.time import is_before, parse_datetime
from app_settings import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD

db_uri = f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"

client = MongoClient(db_uri)

db = client['admin']

patients_collection = db['patients']
# each document in the "patients" collection has the following strcuture:
# {
#   "_id": <patient_id>,
#   "deleted": <true/false>,
#   "ehr_id": <ehr_id>,
#   "versions": [
#     {
#       "uid": <version_id>,
#       "created": <date/time>,
#       "contribution_id": <contribution_id>,
#       "data": <PERSON data>
#     },
#     ...
#   ]
# }

contributions_collection = db['contributions']
# each document in the "contributions" collection has the following strcuture:
# {
#   "_id": <contribution_id>,
#   "contribution": <CONTRIBUTION data>
# }

# PyMongoError
# https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html

def create_patient_document(patient_id : str, first_version_id : str, contribution_id : str, patient_data : dict, time_created : datetime) -> dict:
    patient_document = {
        "_id": patient_id,
        "deleted": False,
        "ehr_id": None,
        "versions": [
            create_version_for_patient_document(first_version_id, contribution_id, patient_data, time_created)
        ]
    }
    return patient_document

def create_version_for_patient_document(version_id : str, contribution_id : str, patient_data : dict, time_created : datetime) -> dict:
    version_for_patient_document = {
        "uid": version_id,
        "created": time_created.isoformat(),
        "contribution_id": contribution_id,
        "data": patient_data
    }
    return version_for_patient_document

def is_deleted_in_patient_document(patient_document : dict) -> bool:
    return patient_document["deleted"]

def get_first_version_id_from_patient_document(patient_document : dict) -> bool:
    return patient_document["versions"][0]["uid"]

def get_most_recent_version_id_from_patient_document(patient_document : dict) -> bool:
    return patient_document["versions"][-1]["uid"]

def get_ehr_id_from_patient_document(patient_document : dict) -> str:
    return patient_document.get("ehr_id", None)

def find_version_id_by_time_in_patient_document(patient_document : dict, time : str) -> str:
    for patient_version in reversed(patient_document["versions"]):
        record_time = patient_version["created"]
        if is_before(record_time, time):
            version_id = patient_version["uid"]
            return version_id
    return None

def find_version_in_patient_document(patient_document : dict, version_id : str) -> Tuple[str, str, datetime, str, dict]:
    preceding_version_id = None
    for patient_version in patient_document["versions"]:
        current_version_id = patient_version["uid"]
        if current_version_id == version_id:
            creation_time = parse_datetime(patient_version["created"])
            return (current_version_id, preceding_version_id, creation_time, patient_version["contribution_id"], patient_version["data"])
        else:
            preceding_version_id = current_version_id
    return (None, None, None, None, None)

def insert_patient_document(patient_id : str, first_version_id : str, contribution_id : str, patient_data : dict, time_created : datetime, transaction : ClientSession = None):
    patient_document = create_patient_document(patient_id, first_version_id, contribution_id, patient_data, time_created)
    try:
        patients_collection.insert_one(
            document = patient_document,
            session = transaction
        )
        return True
    except pymongo_errors.DuplicateKeyError:
        return False

def set_ehr_id_of_patient_document(patient_id : str, ehr_id : str, transaction : ClientSession = None) -> str:
    update_result = patients_collection.update_one(
        filter = {
            "_id": patient_id
        },
        update = {
            "$set": {
                "ehr_id": ehr_id
            }
        },
        session = transaction
    )

def add_version_to_patient_document(patient_id : str, version_id : str, contribution_id : str, patient_data : dict, time_created : datetime, transaction : ClientSession = None):
    version = create_version_for_patient_document(version_id, contribution_id, patient_data, time_created)
    update_result = patients_collection.update_one(
        filter = {
            "_id": patient_id
        },
        update = {
            "$push": {
                "versions": version
            }
        },
        session = transaction
    )

def find_all_patient_ids(transaction : ClientSession = None):
    cursor = patients_collection.find(
        filter = {},
        session = transaction
    )
    patient_ids = []
    for patients_document in cursor:
        patient_id = patients_document["_id"]
        patient_ids.append(patient_id)
    return patient_ids

def find_patient_document(patient_id : str, transaction : ClientSession = None) -> dict:
    return patients_collection.find_one(
        filter = {
            "_id": patient_id
        },
        session = transaction
    )

def set_deleted_in_patient_document(patient_id : str, deleted : bool, transaction : ClientSession = None):
    update_result = patients_collection.update_one(
        filter = {
            "_id": patient_id
        },
        update = {
            "$set": {
                "deleted": deleted
            }
        },
        session = transaction
    )

def extract_contribution_from_contribution_document(contribution_document : dict) -> dict:
    return contribution_document["data"]

def insert_contribution_document(contribution_id : str, contribution : dict, transaction : ClientSession = None):
    contribution_document = {
        "_id": contribution_id,
        "data": contribution
    }
    insert_result = contributions_collection.insert_one(
        document = contribution_document,
        session = transaction
    )

def find_contribution_document(contribution_id : str, transaction : ClientSession = None) -> dict:
    return contributions_collection.find_one(
        filter = {
            "_id": contribution_id
        },
        session = transaction
    )

supportsSession = None

@contextmanager
def begin_transaction() -> ClientSession:
    global supportsSession
    if supportsSession is None:
        serverVersion = tuple(client.server_info()['version'].split('.'))
        if int(serverVersion[0]) > 3 or (int(serverVersion[0]) == 3 and int(serverVersion[1]) >= 6):
            supportsSession = True
        else:
            supportsSession = False

    if supportsSession:
        with client.start_session() as session:
            with session.start_transaction():
                yield session
    else:
        yield None
