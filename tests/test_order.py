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
    
    # def test_post_menu(self):
    #     """
    #     Test API can create a category (POST request)
    #     """
    #     # register a test user, then log them in
    #     self.TestAdminAuthentication.register_user()
    #     result = self.login_user()
    #     # obtain the access token
    #     access_token = json.loads(result.data.decode())['access_token']
    #     # ensure the request has an authorization header set with the access token in it
    #     res = self.client().post(
    #         '/api/v1/categories/',
    #         headers=dict(Authorization="Bearer " + access_token),
    #         data = self.category)
    #     self.assertEqual(res.status_code, 201)
    #     self.assertIn('salad', str(res.data))


    # # def test_get_all_orders(self):
    # #     result = self.client().get('/api/v1/orders',headers={'Authorization':self.login()})
    # #     raise Exception(result)
    # #     self.assertEqual(result.status_code, 200)


    # def test_add_order(self):
    #     """ test for posting an order """
    #     add_result = self.client().post('/api/v1/orders', content_type='application/json',
    #                                 data=json.dumps(dict(username="moses",
    #                                                      phone_number="0704893645", order_items="['matooke']")))
    #     self.assertEqual(add_result.status_code, 201)    



    # def test_api_gets_all_orders(self):
    #     """
    #     Test API can get all (GET request).
    #     """
    #     response = self.client().get('/api/v1/admin/orders',
    #                                  headers=({"Authorization": "Bearer " + self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.json['orders'], list)
    #     self.assertIn("results retrieved successfully", response.json["message"])

    # # def test_api_gets_user_order(self):
    #     """
    #     Test API can get all orders for a single user.
    #     """
    #     response = self.client().get('/api/v1/orders',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.json['orders'], list)
    #     self.assertIn("results retrieved successfully", response.json["message"])

    # def test_get_one_order(self):
    #     """
    #     Test REturn Of Single Order.
    #     """
    #     response = self.client().get('/api/v1/orders/1',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("order", response.json)
    #     self.assertIn("result retrieved successfully", response.json["message"])
    #     self.assertIsInstance(response.json['order'], dict)
    #     self.assertEqual(len(response.json['order']), 8)

    # def test_order_attributes_returned(self):
    #     """
    #     Test that all values expected  in an order dictionary are returned
    #     """
    #     response = self.client().get('/api/v1/orders/1',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertIn(1, response.json['order'].values())
    #     self.assertIn("1", response.json['order']["quantity"])
    #     self.assertEqual(2, response.json['order']["totalamount"])
    #     self.assertEqual(self.payment_mode, response.json['order']["payment_mode"])
    #     self.assertEqual(self.order_status, response.json['order']["order_status"])

    # def test_order_not_found(self):
    #     """
    #     Test API returns nothing when an order is not found
    #     A return contsins a status code of 200
    #     """
    #     response = self.client().get('/api/v1/orders/7',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual("No order available with id: 7", response.json['message'])

    

    # def test_post_creates_order(self):
    #     """
    #     This method tests for the creation of an
    #     """
    #     response = self.client().post('/api/v1/orders/', data=json.dumps(
    #         self.ride3.__dict__), content_type='application/json',
    #                                   headers=({"auth_token": self.generate_token()}))

    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn("order", response.json)
    #     self.assertEqual("Order added successfully", response.json['message'])
    #     self.assertTrue(response.json['order'])

    # def test_order_exists_already(self):
    #     """
    #     This method tests that a duplicate of an order is not added to
    #     the system
    #     """
    #     response = self.client().post('/api/v1/orders', data=json.dumps(
    #         self.order1.__dict__), content_type='application/json',
    #                                   headers=({"decoded": self.generate_token()}))

    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual("Order already exists", response.json["message"])

    # # def test_non_json_data_not_sent(self):
    #     """
    #     This method tests that non json data is not sent
    #     """
    #     response = self.client().post('/api/v1/user/orders', data=json.dumps(
    #         self.ride1.__dict__), content_type='text/plain',
    #                                   headers=({"auth_token": self.generate_token()}))

    #     self.assertEqual(response.status_code, 400)
    #     self.assertTrue(response.json)
    #     self.assertEqual("content not JSON", response.json['error_message'])

    # # def test_empty_attributes_not_sent(self):
    # #     """
    # #     This method tests that data is not sent with empty fields
    # #     """
    # #     response = self.client().post('/api/v1/orders', data=json.dumps(
    # #         dict(order_id=2,
    # #              quantity= ,
    # #              payment_mode="Mobile Money",
    # #              order_status="")), content_type='application/json',
    # #                                   headers=({"auth_token": self.generate_token()}))

    # #     self.assertEqual(response.status_code, 400)
    # #     self.assertTrue(response.json)
    # #     self.assertEqual("Some fields are empty", response.json['error_message'])

    # def test_partial_fields_not_sent(self):
    #     """
    #     This method tests that data with partial fields is not sent
    #     on creating an order
    #     """
    #     response = self.client().post('/api/v1/orders', data=json.dumps(
    #         dict(quantity=3, totalamount=2)),
    #                                   content_type='application/json',
    #                                   headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual("some of these fields are missing",
    #                      response.json['error_message'])

    # def test_post_joins_a_ride_offer(self):
    #     """
    #     This method tests the joinig of a ride offer
    #     (POST request)
    #     """
    #     response = self.client().post('/api/v1/rides/1/requests',
    #                                   headers=({"auth_token": self.get_another_token()}))

    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn("request", response.json)
    #     self.assertEqual("request sent successfully", response.json['message'])
    #     self.assertTrue(response.json['request'])

    # def test_request_exists_already(self):
    #     """
    #     Tests that a request is not duplicated if it exists already
    #     (POST request)
    #     """
    #     response = self.client().post('/api/v1/rides/1/requests',
    #                                  content_type='application/json',
    #                                   headers=({"auth_token": self.generate_token()}))

    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual("Request already exists", response.json["message"])

    # def test_non_existing_ride_request(self):
    #     """
    #     This method tests that a request made to a non existing
    #     ride offer returns a JSON response showing ride not
    #     found
    #     """
    #     response = self.client().post('/api/v1/rides/22/requests',
    #                                   headers=({"auth_token": self.generate_token()}))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual("No ride available with id: 22", response.json['message'])

    # def test_api_gets_all_ride_requests(self):
    #     """
    #     Test API can get all ride requests (GET request).
    #     """
    #     response = self.client().get('/api/v1/users/rides/1/requests',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("result retrieved successfully", response.json["message"])

    # def test_getting_user_ride_requests(self):
    #     """
    #     Test API returns requests made by a sinle user.
    #     """
    #     response = self.client().get('/api/v1/user/requests',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("result retrieved successfully", response.json["message"])

    # def test_editing_json_format(self):
    #     """
    #     This method tests whether a request sent to make an update
    #     is a JSON format. An error is returned if the format  is
    #     not JSON
    #     """
    #     response = self.client().put('/api/v1/users/rides/1/requests/1',
    #                                  data=json.dumps(dict(request_status="Accepted")),
    #                                  content_type='text/plain',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual("Content-type must be JSON", response.json["message"])

    # def test_edit_existing_ride(self):
    #     """
    #     This method tests whether an update is made to a request
    #     of an existing ride. A message of no ride available is returned
    #     if a ride offer doesnot exist.
    #     """
    #     response = self.client().put('/api/v1/users/rides/5/requests/1',
    #                                  data=json.dumps(dict(request_status="Accepted")),
    #                                  content_type='application/json',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual("No ride available with id: 5", response.json['message'])

    # def test_edit_existing_request(self):
    #     """
    #     This method tests whether an update is made to a request
    #     an existing request. A message of no request available is
    #     returned if a request doesnot exist.
    #     """
    #     response = self.client().put('/api/v1/users/rides/1/requests/10',
    #                                  data=json.dumps(dict(request_status="Accepted")),
    #                                  content_type='application/json',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual("No request available with id: 10", response.json['message'])

    # def test_edit_request(self):
    #     """
    #     This method tests whether a request status is updated.
    #     default is pending and can be updated to Accepetd or
    #     rejected.
    #     """
    #     response = self.client().put('/api/v1/users/rides/1/requests/1',
    #                                  data=json.dumps(dict(request_status="Accepted")),
    #                                  content_type='application/json',
    #                                  headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual("success", response.json["status"])

    # def test_invalid_token(self):
    #     """
    #     This method tests whether api rejects invalid token.
    #     """
    #     response = self.client().get('/api/v1/user/requests',
    #                                  headers=({"auth_token": "xxxxxvvvvvv"}))
    #     self.assertEqual(response.status_code, 401)
    #     self.assertEqual("Invalid token. Please log in again.", response.json["message"])

    # def test_token_missing(self):
    #     """
    #     This method tests whether api rejects requests
    #     with missing tokens.
    #     """
    #     response = self.client().get('/api/v1/rides/')
    #     self.assertEqual(response.status_code, 401)
    #     self.assertEqual("Token is missing", response.json["message"])

    # def test_user_not_loogedin(self):
    #     """
    #     This method tests that a logged out user doesnot access the end point
    #     """
    #     user_token = self.generate_token()
    #     self.client().post('/api/v1/users/logout',
    #                        headers=({"auth_token": user_token}))
    #     response = self.client().post('/api/v1/users/logout',
    #                                   headers=({"auth_token": user_token}))
    #     self.assertEqual(response.status_code, 401)
    #     self.assertEqual("Please login", response.json["message"])


    # def test_logout(self):
    #     """
    #     This method tests that a user is able to logout
    #     """
    #     response = self.client().post('/api/v1/users/logout',
    #                                   headers=({"auth_token": self.generate_token()}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual("You are logged out successfully", response.json["message"])

    # def test_login_status(self):
    #     """
    #     This method tests the status of a user when logged in
    #     """
    #     response = self.user_obj.check_login_status(1)
    #     self.assertEqual(True, response)

    # def test_logout_status(self):
    #     """
    #     This method tests the user status after logging out
    #     of the system. Firts logs out the user and then checks user
    #     status.
    #     """
    #     self.client().post('/api/v1/users/logout',
    #                        headers=({"auth_token": self.generate_token()}))
    #     response = self.user_obj.check_login_status(1)
    #     self.assertEqual(False, response)












    # def tearDown(self):
    #     sql_commands = (
    #         """DROP TABLE IF EXISTS "users" CASCADE;""",
    #         """DROP TABLE IF EXISTS "order" CASCADE;""",
    #         """DROP TABLE IF EXISTS "menu" CASCADE;""")
    #     conn = None
    #     try:
    #         conn = DBAccess.db_connection()
    #         cur = conn.cursor()
    #         for sql_command in sql_commands:
    #             cur.execute(sql_command)
    #         cur.close()
    #         conn.commit()
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if conn is not None:
    #             conn.close()

