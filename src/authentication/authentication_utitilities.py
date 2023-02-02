# *************************************
# SpeedCollect
# Web Service
# 'authentication_utilities.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from flask import session
from database.database_connection import database
import utilities.constants as constants
from functools import wraps

def username_exists(username: str) -> bool:

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { 'username': username } ) != None

def email_exists(email: str) -> bool:

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { 'email': email } ) != None

def get_user_by_email(email: str):

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { 'email': email } )

def get_user_by_user_id(user_id: str):

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { 'user_id': user_id } )

# Authentication Decorator
def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        try:
           
            user_id = session.get(constants.USER_ID)

            if(not user_id):
                return {
                    'error-message': 'user-not-authenticated'
                }, constants.HTTP_UNAUTHORIZED_CODE

        except:
            
            return {
                'error-message': 'user-not-authenticated'
            }, constants.HTTP_UNAUTHORIZED_CODE

        return f(*args, **kwargs)

    return decorator
    