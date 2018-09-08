"""
A module that provides responses to url requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from api.models.ordersv1 import Ordersv1Handler

class OrderViews(MethodView):
    """
    Class with Methods For Responding To url End Points.
    """
    ordersv1_handler = Ordersv1Handler()
    def get(self, order_id):
        """
         Method That Returns Specific Order When an Id is Specified
        """
        if not order_id:
            return jsonify({"status_code": 400, "data": str(request.data),
                            "error_message": "No Specified Order"}), 400
        return self.ordersv1_handler.return_specific_order(order_id)
