"""
Module For Handling Error Messages.
"""
from flask import jsonify


class ErrorMessage(object):
    """
    Class Contains Methods For Handling Error Messages.
    """

    def fields_missing_information(self, request_data):
        """
        Method Returns Response When Some Fields Are Empty
        """
        return jsonify({"status": "failure",
                        "status_code": 400, "data": request_data,
                        "error_message": "Some Fields Are Empty"}), 400

    def request_missing_fields(self):
        """
        Method Returns Response When Some Fields Are Missing
        """
        return jsonify({"status": "failure",
                        "error_message": "Some Fields Are Missing"}), 400

    def no_order_available(self, order_id):
        """
        Method Returns JSON Response If Order Not Found
        """
        return jsonify({"status": "failure",
                        "message": "No Order Available With Id: " + str(order_id)}), 200

    def no_user_found_response(self, message, user_id):
        """
        Method Returns Error Message When User Not Found For Particular Id
        """
        return jsonify({"status": "failure",
                        "message": message,
                        "error_message": "No User Found with id: " + str(user_id)
                       }), 400

    def no_menu_found(self, item_id):
        """
        Returns Message If No Menu Item Found for Specified Id
        """
        return jsonify({"status": "failure",
                        "message": "No Menu Item Found With Id: " + str(item_id)}), 200
                        