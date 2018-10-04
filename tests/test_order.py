"""
This module contains tests for the api end points.
"""
from unittest import TestCase
from datetime import datetime
from flask import json
import psycopg2
from api import APP
from api.models.user import User
from api.models.orders import Order
from api.models.db_connection import DBAccess
from tests.test_authentication import TestAdminAuthentication
import pytest, psycopg2
from werkzeug.security import check_password_hash

@pytest.fixture
def test_client():
     return APP.test_client()

@pytest.fixture
def connection():
    conn = psycopg2.connect(
        dbname='FastFoodFast',
        user='postgres', 
        host='localhost',
        password='moses12',
        port='5433'
    )
    return conn

def register_and_login_user(email_address, password, test_client):
    user_data = {'email_address': email_address, 'password': password}
    test_client.post('/api/v1/auth/signup', json=user_data)
    response = test_client.post('/api/v1/auth/login', json=user_data)
    token = response.get_json()['token']
    headers = {'Authorization': 'Bearer ' + token}
    return headers

def login_administrator(test_client):
    admin = {'email_address': 'moses', 'password': 'moses12'}
    response = test_client.post('/api/v1/admin/login', json=admin)
    token = response.get_json()['token']
    headers = {'Authorization': 'Bearer ' + token}
    return headers

def test_api_returns_error_message_given_wrong_registration_data(test_client):
    invalid_user_data = {'email_address': '  ', 'password': 'mypass'}
    response = test_client.post('/api/v1/auth/signup', json=invalid_user_data)
    assert response.status_code == 400
    assert response.data 