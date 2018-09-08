"""
A module that provides responses to url requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from api.models.ordersv1 import Ordersv1Handler

class OrderViews(MethodView):
    """
    Class with Methods For Responding To Various url End Points.
    """
    ordersv1_handler = Ordersv1Handler()
    def post(self):
        """"
        Methd For Handling Post Requests
        """
        if not request or not request.json:
            return jsonify({"status_code": 400, "data": str(request.data),
                            "error_message": "content not JSON"}), 400
        return self.ordersv1_handler.post_orderv1()
