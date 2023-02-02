# *************************************
# SpeedCollect
# Web Service
# 'login.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from werkzeug.security import check_password_hash
import utilities.constants as constants
import authentication.authentication_utitilities as auth

def password_matches(email: str, password: str) -> bool:

    user = auth.get_user_by_email(email) 

    hashed_password = user[constants.PASSWORD]

    return check_password_hash(pwhash=hashed_password, password=password)
    