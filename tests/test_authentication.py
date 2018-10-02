"""
Module To Test User Account Creatiom/ Signing In.
"""
import uuid
from unittest import TestCase
from flask import json
import psycopg2
from api.models.user import User
from api import APP
from api.models.db_connection import DBAccess

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client

class TestUserAuthentication(TestCase):
    """
    Tests For API End Points.
    """
    user1 = User("moses", "kamira",
                 "moses.african@gmail.com", "0789608543", "moses")
    empty_user = User("", "",
                      "moses.african@gmail.com", "0789608543", "moses")
    def setUp(self):
        """
        Defining Test Variables, Initialize APP.
        """
        APP.config['TESTING'] = True
        self.app = APP
        self.client = self.app.test_client
        DBAccess.create_databasetables()

    def test_app_variable_config(self):
        """
        Method For Tests App Configuration Variables
        """
        self.assertNotEqual(APP.config['SECRET_KEY'], "I-Love_Andela")
        self.assertTrue(APP.config['DEBUG'] is True)
        self.assertTrue(APP.config['TESTING'] is True)
    
    def test_partial_fields_not_sent(self):
        """
        Method For Testing That Data With Partial Fields Is Not Sent
        """
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(
            dict(first_name=self.user1.first_name,
                 last_name=self.user1.last_name, email_address=self.user1.email_address)),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual("Some Fields Are Missing",
                         response.json['error_message'])
    
    def test_empty_attributes_not_sent(self):
        """
        Method That Empty Fields Are Not Sent
        """
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(
            self.empty_user.__dict__), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.json)
        