# *************************************
# SpeedCollect
# Web Service
# '__main__.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

from flask import Flask

app = Flask(__name__)

import authentication.authentication_endpoints
import utilities.constants as constants

if __name__ == '__main__':
    app.run(host=constants.SERVER_IP, port=constants.SERVER_PORT, debug=True)