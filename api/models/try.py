"""
This module is a User model with its attributes
"""
import re
import datetime
from flask import jsonify
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import psycopg2
import jwt
from api.models.db_transaction import DbTransaction
from api.models.db_connection import DBAccess


class User(object):
    """
    Class Represents User Entity
    """
    def __init__(self, *args):
        if args:
            self.first_name = args[0]
            self.last_name = args[1]
            self.email_address = args[2]
            self.phone_number = args[3]
            self.password = args[4]

    def save_user(self):
        """
        Method For Saving User Instance In Database Table.
        """

        user_data = (self.first_name, self.last_name,
                     self.email_address, self.phone_number, self.password)
        user_sql = """INSERT INTO users(first_name, last_name, email_address, phone_number, password) VALUES( %s, %s, %s, %s, %s) RETURNING user_id;"""
        DbTransaction.save(user_sql, user_data)
    def return_user_details(self):
        """
        Method Returns User Details
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email_address": self.email_address,
            "phone_number": self.phone_number,
            "password": self.password
        }

    def verify_user_on_signup(self, user_request):
        """
        Method For Verifing User During Creation of Account
        """
        keys = ("first_name", "last_name", "email_address",
                "phone_number", "password")
        if not set(keys).issubset(set(user_request)):
            return {"status": "failure",
                    "error_message": "Some Fields Are Missing"}

        user_condition = [
            user_request["first_name"].strip(),
            user_request["last_name"].strip(),
            user_request["email_address"].strip(),
            user_request["phone_number"].strip(),
            user_request["password"].strip()
        ]

        if not all(user_condition):
            return {"status": "failure",
                    "error_message": "Some Fields Are Empty"}

        if re.match(r"[^@]+@[^@]+\.[^@]+", user_request["email_address"]):
            return {"status": "success",
                    "message": "Valid Details"}

        return {"status": "failure",
                "error_message": "Missing or Incorrect E-mail Address Format"}

    def update_user_status(self, status, user_id):
        """
        Method For Updating User Login Status
        """
        user_status_update_sql = """UPDATE users SET is_loggedin = %s
                    WHERE user_id = %s"""
        if status:
            edit_data = (True, user_id)
        else:
            edit_data = (False, user_id)
        DbTransaction.edit(user_status_update_sql, edit_data)
        if status:
            return None
        return {"status": "success",
                'message': 'You Are Successfully Logged Out'}

    def encode_token(self, user_id):
        """
        Generates Authentication Token
        """
        from api import APP
        
        # try:
        #     token = jwt.JWT.encode({"user_id": user_id,
        #                         "exp": datetime.datetime.utcnow() +
        #                                datetime.timedelta(minutes=2000)},
        #                        APP.secret_key)
        #     return token
        # except Exception as error:
        #     return error
        try:
            token = jwt.encode({'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow()
            }, APP.secret_key)
            
            return (token,
            APP.secret_key)
        except Exception as e:
            return e

    def decode_token(self, auth_token):
        """
        Decodes Authentication Token
        """
        from api import APP
        try:
            token = jwt.decode(auth_token, APP.secret_key)
            return token['user_id']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
        # try:
        #     token = jwt.JWT.decode(auth_token, APP.config.get("SECRET_KEY"))
        #     return {"user_id": token["user_id"],
        #             "state": "Success"}
        # except(Exception, psycopg2.DatabaseError) as error:
        #     print(error)

    def decode_failure(self, message):
        """
        Method Returns Error Message When an Error Is
        Encounterd on Decoding Token
        """
        return jsonify({"message": message}), 401

    def check_login_status(self, user_id):
        """
        Method For Checking Whether User Is Logged In or Not
        """
        is_loggedin = DbTransaction.fetch_one(
            """SELECT "is_loggedin" FROM "users" WHERE "user_id" = %s""",
            (user_id, ))
        if is_loggedin[0]:
            return True
        return False
