# *************************************
# SpeedCollect
# Web Service
# 'constants.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

# Web Service Constants

# HTTP Status codes
HTTP_OK_CODE = 200
HTTP_BAD_REQUEST_CODE = 400
HTTP_UNAUTHORIZED_CODE = 401
HTTP_NOT_FOUND_CODE = 404
HTTP_CONFLICT_CODE = 409
HTTP_INTERNAL_ERROR_CODE = 500

# Server constans
SERVER_IP = '0.0.0.0'
SERVER_PORT = 5000

# Strings
DB_SESSIONS_COLLECTION = 'Sessions'
DB_USERS_COLLECTION = 'Users'
DB_COLLECTIONS_COLLECTION = 'Collections'
DB_ITEMS_COLLECTION = 'Items'
CONTENT_TYPE = 'Content-Type'
USER_ID = 'user_id'
USERNAME = 'username'
EMAIL = 'email'
PASSWORD = 'password'
OBJECT_ID = '_id'
COLLECTION_ID = "collection_id"
COLLECTION_NAME = 'collection_name'
COLLECTION_TYPE = 'collection_type'
COLLECTION_DESCRIPTION = 'collection_description'

# Literals
MIN_USERNAME_SIZE = 4
MAX_USERNAME_SIZE = 30
MIN_PASSWORD_SIZE = 8
MAX_PASSWORD_SIZE = 50
MIN_COLLECTION_NAME_SIZE = 1
MAX_COLLECTION_NAME_SIZE = 50
MIN_COLLECTION_TYPE_SIZE = 1
MAX_COLLECTION_TYPE_SIZE = 50
MIN_COLLECTION_DESCRIPTION_SIZE = 1
MAX_COLLECTION_DESCRIPTION_SIZE = 400
SESSION_LIFETIME_DAYS = 1
