# *************************************
# SpeedCollect
# Web Service
# 'authentication_endpoints.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from __main__ import app
from bson.json_util import dumps
from flask import request
import utilities.constants as constants
import authentication.login as login


# Register User Endpoint
@app.put("/backend-api/register")
def register_user():

    try:

        # Verify JSON Content Type
        if(not request.is_json):
            return {
                'error-message': 'content-not-application-json'
            }, constants.HTTP_BAD_REQUEST_CODE

        user_data = request.get_json()

        if(not((constants.USERNAME in user_data) and (constants.EMAIL in user_data) and (constants.PASSWORD in user_data))):
            return {
                'error-message': 'missing-fields'
            }, constants.HTTP_BAD_REQUEST_CODE

        username = user_data[constants.USERNAME]
        email = user_data[constants.EMAIL]
        password = user_data[constants.PASSWORD]

        if(not login.valid_username(username)):
            return {
                'error-message': 'invalid-username'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(not login.valid_email(email)):
            return {
                'error-message': 'invalid-email'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(not login.valid_password(password)):
            return {
                'error-message': 'invalid-password'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(login.username_exists(username)):
            return {
                'error-message': 'username-exists'
            }, constants.HTTP_INTERNAL_ERROR_CODE

        if(login.email_exists(email)):
            return {
                'error-message': 'email-exists'
            }, constants.HTTP_INTERNAL_ERROR_CODE

        return dumps(login.register_user(username, email, password)), constants.HTTP_OK_CODE

    except:

        return {
            'error-message': 'register-error'
        }, constants.HTTP_INTERNAL_ERROR_CODE