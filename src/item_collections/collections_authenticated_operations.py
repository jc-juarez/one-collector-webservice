# *************************************
# SpeedCollect
# Web Service
# 'collections_authenticated_operations.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from database.database_connection import database
import utilities.constants as constants
import uuid

def user_has_same_collection(user_id: str, collection_name: str) -> bool:

    collections_collection = database[constants.DB_COLLECTIONS_COLLECTION]

    return collections_collection.find_one( { 'user_id': user_id, 'collection_name': collection_name } ) != None

def get_collection_by_user_id_and_collection_name(user_id: str, collection_name: str) -> bool:

    collections_collection = database[constants.DB_COLLECTIONS_COLLECTION]

    return collections_collection.find_one( { 'user_id': user_id, 'collection_name': collection_name } )

def create_collection(user_id: str, collection_name: str, collection_type: str, collection_description: str):

    collection = {
        "collection_id": str(uuid.uuid4()),
        "user_id": user_id,
        "collection_name": collection_name,
        "collection_type": collection_type,
        "collection_description": collection_description
    }

    collections_collection = database[constants.DB_COLLECTIONS_COLLECTION]
    collections_collection.insert_one(collection)