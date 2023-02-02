# *************************************
# SpeedCollect
# Web Service
# '__main__.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from flask import Flask
from flask_sessionstore import Session
from datetime import timedelta
from database.database_connection import database_client
import utilities.constants as constants
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.getenv('SECRETKEY'))
app.config['SESSION_TYPE'] = 'mongodb'
app.config['SESSION_MONGODB'] = database_client
app.config['SESSION_MONGODB_DB'] = str(os.getenv('DBNAME'))
app.config['SESSION_MONGODB_COLLECT'] = constants.DB_SESSIONS_COLLECTION
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=constants.SESSION_LIFETIME_DAYS)
app.config['SESSION_USE_SIGNER'] = True

server_session = Session(app)

import authentication.authentication_endpoints

if __name__ == '__main__':
    app.run(host=constants.SERVER_IP, port=constants.SERVER_PORT, debug=True)