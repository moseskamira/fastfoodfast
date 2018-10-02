"""
Module For Handling Errors Upon Hiting Wrong API End Point.
"""
from flask import jsonify, request


class ErrorHandler(object):
    """
    Class For Handling Request Errors Upon Sending Wrong url.
    """
    @staticmethod
    def url_not_found(status_code=None):
        """
        Method Returns Error Message In Json Format.
        """
        if status_code:

            message = {
                "error_message": "Requested Resource Not Found On Server",
                "status_code": 404,
                "url":  request.url
            }
            response = jsonify(message)
            response.status_code = 404
        return response
