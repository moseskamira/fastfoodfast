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


class TestOrder(TestCase):
    """
    Test Runs For Api Endpoints.
    """

    date_time = datetime.now()
    depart_date = date_time.strftime("%x")
    depart_time = date_time.strftime("%H:%M")

    user1 = User("Moses", "Kamira", "moses.african@gmail.com", "0789608543", "moses12")
    user2 = User("shamim", "Natebwa", "shamynat@gmail.com", "0705676543", "kenth")
    user_object = User()

    order1 = Order(
        1, 4, 678000, "Mobile Money", "pending")
    order2 = Order(
        2, 6, 67000, "Cash", "pending")

    def setUp(self):
        """
        Define Test Variables
        Initialize App
        """
        APP.config['TESTING'] = True
        self.app = APP
        self.client = self.app.test_client
        DBAccess.create_databasetables()
        self.client().post('/api/v1/auth/signup', data=json.dumps(
            self.user1.__dict__), content_type='application/json')
        self.client().post('/api/v1/auth/signup', data=json.dumps(
            self.user2.__dict__), content_type='application/json')
   

    def test_error_hander_returns_json(self):
        """
        Test API returns a json format response when the user hits
        a wrong api end point
        """
        response = self.client().get('/api/v1/admin/orders/myserver')
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json, dict)
        self.assertEqual("Requested Resource Not Found On Server",
                         response.json["error_message"])
        self.assertEqual("http://localhost/api/v1/admin/orders/myserver",
                         response.json["url"])
        """
        

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

