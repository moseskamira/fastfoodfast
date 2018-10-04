"""
This module is a User model with its attributes
"""
import re
import datetime
from flask import jsonify, request
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import psycopg2
import jwt
from api.models.db_transaction import DbTransaction
from api.models.db_connection import DBAccess


class Admin(object):
    """
    Class Represents Admin Entity
    """
    def __init__(self, *args):
        if args:
            self.first_name = args[0]
            self.last_name = args[1]
            self.email_address = args[2]
            self.phone_number = args[3]
            self.password = args[4]

    def save_admin(self):
        """
        Method For Saving Admin Instance In Database Table.
        """

        admin_data = (self.first_name, self.last_name,
                     self.email_address, self.phone_number, self.password)
        admin_sql = """INSERT INTO admin(first_name, last_name, email_address, phone_number, password) VALUES( %s, %s, %s, %s, %s) RETURNING admin_id;"""
        DbTransaction.save(admin_sql, admin_data)
    def return_admin_details(self):
        """
        Method Returns Admin Details
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email_address": self.email_address,
            "phone_number": self.phone_number,
            "password": self.password
        }

    def verify_admin_on_signup(self, admin_request):
        """
        Method For Verifing Admin During Creation of Account
        """
        keys = ("first_name", "last_name", "email_address",
                "phone_number", "password")
        if not set(keys).issubset(set(admin_request)):
            return {"status": "failure",
                    "error_message": "Some Fields Are Missing"}

        admin_condition = [
            admin_request["first_name"].strip(),
            admin_request["last_name"].strip(),
            admin_request["email_address"].strip(),
            admin_request["phone_number"],
            admin_request["password"]
        ]

        if not all(admin_condition):
            return {"status": "failure",
                    "error_message": "Some Fields Are Empty"}

        if re.match(r"[^@]+@[^@]+\.[^@]+", admin_request["email_address"]):
            return {"status": "success",
                    "message": "Valid Details"}

        return {"status": "failure",
                "error_message": "Incorrect E-mail Address Format"}

    def update_admin_status(self, status, admin_id):
        """
        Method For Updating Admin Login Status
        """
        admin_status_update_sql = """UPDATE admin SET is_loggedin = %s
                    WHERE admin_id = %s"""
        if status:
            edit_data = (True, admin_id)
        else:
            edit_data = (False, admin_id)
        DbTransaction.edit(admin_status_update_sql, edit_data)
        if status:
            return None
        return {"status": "success",
                'message': 'You Are Successfully Logged Out'}

    def encode_token(self, admin_id):
        """
        Generates Authentication Token
        """
        from api import APP

        try:
            token = jwt.encode({'admin_id': admin_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5345678888),
            'iat': datetime.datetime.utcnow()
            }, APP.secret_key)
            
            return token
        except Exception as e:
            return e

    def decode_token(self, token):
        """
        Decodes Authentication Token
        """
        from api import APP
        try:
            token = jwt.decode(token, APP.secret_key)
            print(token['admin_id'])
            return token['admin_id']
        except jwt.ExpiredSignatureError:
            return 'Signature Expired. Please Log In Again.'
        except jwt.InvalidTokenError:
            return 'Invalid Token. Please log In Again.'

    def decode_failure(self, message):
        """
        Method Returns Error Message When an Error Is
        Encounterd on Decoding Token
        """
        return jsonify({"message": message}), 401

    def check_login_status(self, admin_id):
        """
        Method For Checking Whether Admin Is Logged In or Not
        """
        is_loggedin = DbTransaction.fetch_one(
            """SELECT "is_loggedin" FROM "admin" WHERE "admin_id" = %s""",
            (admin_id, ))
        if is_loggedin[0]:
            return True
        return False
