"""
Module For Setting Up up Flask Emvironment
"""
from flask import Flask
from api.handler import ErrorHandler
from flask_cors import CORS
from api.config import ENVIRONMENT, TESTING, SECRET_KEY, DEBUG
from api.urls import Urls
from db_connection import DBAccess

APP = Flask(__name__)
CORS(APP)
APP.secret_key = SECRET_KEY
APP.testing = TESTING
APP.debug = DEBUG
APP.env = ENVIRONMENT
APP.errorhandler(404)(ErrorHandler.url_not_found)

Urls.generate_url(APP)

DBAccess.create_databasetables()

