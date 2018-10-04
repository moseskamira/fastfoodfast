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


class TestUserAuthentication(TestCase):
    """
    Tests For API End Points.
    """
    user1 = User("James", "kisule",
                 "getjamesgrant@gmail.com", "0789608543", "moses")
    empty_user = User("", "",
                      "moses.africafgn@gmail.com", "0789608543", "moses")
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
    
    
    def test_user_registration(self):
        """
        Test Whether User Is Logged In Successfully
        """
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(
            self.user1.__dict__), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.content_type == 'application/json')
        self.assertIn("user", response.json)
        self.assertEqual("New User Successfully Registered", response.json['message'])
        self.assertTrue(response.json['user'])

    def test_content_type_not_json(self):
        """
        Test that the content type that is not application/json
        """
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(
            self.user1.__dict__), content_type='text/plain')

        self.assertEqual(response.status_code, 400)
        self.assertEqual("Failed Content-Type Must Be Json", response.json['error'])
    
    def test_empty_attributes_not_sent(self):
        """
        Method Tests That Data Is Not Sent With Empty Fields
        """
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(
            self.empty_user.__dict__), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.json)
        self.assertEqual("Some Fields Are Empty", response.json['error_message'])
    
    # def test_user_login(self):
    #     """
    #     Test For Login of Registered User
    #     """
    #     self.client().post('/api/v1/auth/login', data=json.dumps(
    #         self.user1.__dict__), content_type='application/json')

    #     response = self.client().post(
    #         '/api/v1/auth/login',
    #         data=json.dumps(dict(
    #             email_address=self.user1.email_address,
    #             password=self.user1.password
    #         )),
    #         content_type='application/json'
    #     )

        # # self.assertEqual(response.status_code, 400)
        # self.assertTrue(response.json['message'] == 'Successfully logged In.')
        # self.assertTrue(response.json['auth_token'])
        # self.assertTrue(response.content_type == 'application/json')
        # self.assertEqual(response.status_code, 200)
    
    def test_partial_fields_not_sent(self):
        """
        Method Tests That Partial Fields Are Not Send
        """
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(
            dict(first_name=self.user1.first_name,
                 last_name=self.user1.last_name, email_address=self.user1.email_address)),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual("Some Fields Are Missing",
                         response.json['error_message'])

    
    def tearDown(self):
        sql_commands = (
            """DROP TABLE IF EXISTS "users" CASCADE;""",
            """DROP TABLE IF EXISTS "order" CASCADE;""",
            """DROP TABLE IF EXISTS "menu" CASCADE;""")
        conn = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            for sql_command in sql_commands:
                cur.execute(sql_command)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

