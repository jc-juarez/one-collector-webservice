# *************************************
# SpeedCollect
# Web Service
# 'authentication_endpoints.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from __main__ import app
from bson.json_util import dumps
from flask import request, session
import utilities.constants as constants
import authentication.register as register
import authentication.login as login
import authentication.authentication_utitilities as auth


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

        if(not register.valid_username(username)):
            return {
                'error-message': 'invalid-username'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(not register.valid_email(email)):
            return {
                'error-message': 'invalid-email'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(not register.valid_password(password)):
            return {
                'error-message': 'invalid-password'
            }, constants.HTTP_BAD_REQUEST_CODE

        if(auth.username_exists(username)):
            return {
                'error-message': 'username-exists'
            }, constants.HTTP_CONFLICT_CODE

        if(auth.email_exists(email)):
            return {
                'error-message': 'email-exists'
            }, constants.HTTP_CONFLICT_CODE

        register.register_user(username, email, password)

        user = auth.get_user_by_email(email)

        session[constants.USER_ID] = user[constants.USER_ID]

        user.pop(constants.OBJECT_ID)
        user.pop(constants.USER_ID)
        user.pop(constants.PASSWORD)

        return dumps(user), constants.HTTP_OK_CODE

    except:

        return {
            'error-message': 'register-error'
        }, constants.HTTP_INTERNAL_ERROR_CODE

# Login User Endpoint
@app.post("/backend-api/login")
def login_user():
    
    try:

        # Verify JSON Content Type
        if(not request.is_json):
            return {
                'error-message': 'content-not-application-json'
            }, constants.HTTP_BAD_REQUEST_CODE

        user_login_data = request.get_json()

        if(not((constants.EMAIL in user_login_data) and (constants.PASSWORD in user_login_data))):
            return {
                'error-message': 'missing-fields'
            }, constants.HTTP_BAD_REQUEST_CODE

        email = user_login_data[constants.EMAIL]
        password = user_login_data[constants.PASSWORD]

        if((not auth.email_exists(email)) or (not login.password_matches(email, password))):
            return {
                'error-message': 'email-or-password-incorrect'
            }, constants.HTTP_UNAUTHORIZED_CODE

        user = auth.get_user_by_email(email)

        session[constants.USER_ID] = user[constants.USER_ID]

        user.pop(constants.OBJECT_ID)
        user.pop(constants.USER_ID)
        user.pop(constants.PASSWORD)

        return dumps(user), constants.HTTP_OK_CODE

    except:

        return {
            'error-message': 'login-error'
        }, constants.HTTP_INTERNAL_ERROR_CODE

# Auth Test Endpoint
@app.post("/backend-api/auth")
@auth.login_required
def test_auth():

    user = auth.get_user_by_user_id(session.get(constants.USER_ID))

    print(user)

    return "Auth :)", 200