# *************************************
# SpeedCollect
# Web Service
# 'collections_endpoints.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from __main__ import app
from bson.json_util import dumps
from flask import request, session
import utilities.constants as constants
import authentication.authentication_utitilities as auth
import item_collections.collections_authenticated_operations as auth_ops
import item_collections.collections_public_operations as public_ops
import item_collections.collections_utilities as utils

# Create Collection Endpoint
@app.put("/backend-api/create-collection")
@auth.login_required
def create_collection():

    try:

        # Verify JSON Content Type
        if(not request.is_json):
            return {
                'error-message': 'content-not-application-json'
            }, constants.HTTP_BAD_REQUEST_CODE

        collection_data = request.get_json()

        if(not((constants.COLLECTION_NAME in collection_data) and (constants.COLLECTION_TYPE in collection_data) and (constants.COLLECTION_DESCRIPTION in collection_data))):
            return {
                'error-message': 'missing-fields'
            }, constants.HTTP_BAD_REQUEST_CODE

        collection_name = collection_data[constants.COLLECTION_NAME]
        collection_type = collection_data[constants.COLLECTION_TYPE]
        collection_description = collection_data[constants.COLLECTION_DESCRIPTION]

        if(not utils.valid_collection_name(collection_name)):
            return {
                'error-message': 'invalid-collection-name'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(not utils.valid_collection_type(collection_type)):
            return {
                'error-message': 'invalid-collection-type'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(not utils.valid_collection_description(collection_description)):
            return {
                'error-message': 'invalid-collection-description'
            }, constants.HTTP_BAD_REQUEST_CODE

        user = auth.get_user_by_user_id(session.get(constants.USER_ID))
        user_id = user[constants.USER_ID]

        if(auth_ops.user_has_same_collection(user_id, collection_name)):
            return {
                'error-message': 'collection-exists'
            }, constants.HTTP_CONFLICT_CODE

        auth_ops.create_collection(user_id, collection_name, collection_type, collection_description)

        collection = auth_ops.get_collection_by_user_id_and_collection_name(user_id, collection_name)

        collection.pop(constants.OBJECT_ID)
        collection.pop(constants.USER_ID)
        collection.pop(constants.COLLECTION_ID)

        return dumps(collection), constants.HTTP_OK_CODE

    except:

        return {
            'error-message': 'create-collection-error'
        }, constants.HTTP_INTERNAL_ERROR_CODE