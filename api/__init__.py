"""
Module To Set Up Flask Emvironment
"""
import sys
import os
from flask_cors import CORS
from flask import Flask
from api.handler import ErrorHandler
from api.config import ENVIRONMENT, TESTING
from api.urls import Urls

APP = Flask(__name__)
APP.testing = TESTING
APP.env = ENVIRONMENT
APP.errorhandler(404)(ErrorHandler.url_not_found)

Urls.generate_url(APP)

CORS(APP)
