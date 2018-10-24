"""
Module For Handling User Account Creation
And User Authentication
"""
from flask import request, jsonify
from flask.views import MethodView
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.user import User
from api.models.db_transaction import DbTransaction
from db_connection import DBAccess


class UserRegistration(MethodView):
    """
    Class For Registering User
    """
    user_object = User()

    def post(self):
        """
        Register User, Generate Token
        """
        post_user_data = request.get_json()

        if request.content_type == 'application/json':
            if self.user_object.verify_user_on_signup(post_user_data)["status"] == "failure":
                return jsonify({
                    "error_message": self.user_object.verify_user_on_signup(post_user_data)
                                     ["error_message"]}), 400

            hashed_password = generate_password_hash(post_user_data['password'], method='sha256')

            query = """SELECT * FROM "users" WHERE "email_address" = %s"""
            user_turple = DbTransaction.fetch_one(query, (post_user_data['email_address'], ))

            if not user_turple:
                new_user = User(post_user_data['first_name'], post_user_data['last_name'],
                                post_user_data['email_address'], post_user_data['phone_number'],
                                hashed_password)

                new_user.save_user()
                return jsonify({'message': 'New User Successfully Registered',
                                "user": new_user.return_user_details()}), 201
            return jsonify({"error": 'Failed, User Already Exists,' +
                                             'Please Log In'}), 400
        return jsonify({"status": "failure",
                        "error": "Failed Content-Type Must Be Json"}), 400


class UserLogin(MethodView):
    """
    Class For User To Sign In.
    """
    user = User()

    def post(self):
        """
        Method For Logging In User.
        Genete Token For Authentication of Requests.
        """
        post_user_data = request.get_json()
        requirement = [post_user_data['email_address'].strip(), post_user_data['password']]
        if not all(requirement):
            return jsonify({"status": "failure",
                            'Message': 'All Login Details Required'}), 401

        query = """SELECT * FROM "users" WHERE "email_address" = %s"""
        user = DbTransaction.fetch_one(query, (post_user_data['email_address'], ))
        verified_user = self.verify_user_on_login(user, post_user_data['password'])
       

        if verified_user["status"] == "failure":
            return jsonify({"message": verified_user["error_message"]}), 401
        self.user.update_user_status(True, user[0])
        return jsonify(verified_user), 200
    
    def verify_user_on_login(self, user, password):
        """
        Method For Verifing User Before Accesing App
        """
        if not user:
            return {"status": "failure",
                    'error_message': 'Please Enter Valid Email address'}
        if check_password_hash(user[5], password):
            auth_token = self.user.encode_token(user[0])
            print(auth_token.decode())
            if auth_token:
                response = {"status": "success", "message": "Successfully Logged In.",
                            "auth_Token": auth_token.decode("utf-8")
                           }
                return response
            response = {"status": "failure", "error_message": "Try again"}
            return response

        return {"status": "failure",
                'error_message': 'Please Enter Correct Password'}


class UserLogout(MethodView):
    """
    Class For Loging Out User
    """

    user_object = User()

    def post(self):
        """This method logs out a user"""
        token = request.headers.get('Auth')
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        decoded = self.user_object.decode_token(token)
        if decoded["state"] == "failure":
            return self.user_object.decode_failure(decoded["error_message"])
        if self.user_object.check_login_status(decoded["user_id"]):
            logout_info = self.user_object.update_user_status(False, decoded["user_id"])
            if logout_info["status"] == "success":
                return jsonify(logout_info), 200
            return jsonify({"status": "failure",
                            'error_message': 'Failed to logout'}), 200
        return jsonify({"message": "Please login"}), 401