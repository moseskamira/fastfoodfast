"""
Module For Handling Errors.
"""
from flask import jsonify, request

class ErrorHandler():
    """
    Th For Handling Errors When Wrong urls Are Entered.
    """
    @staticmethod
    def url_not_found(status_code=None):
        """
        This Method returns a formatted 404 error message in json format.
        """
        if status_code:
            message = {
                "error_message": "The requested resource was not found on the server",
                "status_code": 404,
                "url":  request.url
            }
            response = jsonify(message)
            response.status_code = 404
        return response
