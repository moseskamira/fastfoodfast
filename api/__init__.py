"""
Module For Setting Up up Flask Emvironment
"""
from flask import Flask
from api.handler import ErrorHandler
from api.config import ENVIRONMENT, TESTING, SECRET_KEY, DEBUG
from api.urls import Urls
from api.models.db_connection import DBAccess

APP = Flask(__name__)
APP.secret_key = SECRET_KEY
APP.testing = TESTING
APP.debug = DEBUG
APP.env = ENVIRONMENT
APP.errorhandler(404)(ErrorHandler.url_not_found)

Urls.generate_url(APP)
DBAccess.create_databasetables()

