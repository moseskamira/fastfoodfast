"""
Module Handling Requsts For Updating Specific Order Status
"""
from flask import jsonify, request
from flask.views import MethodView
class Ordersv1Handler(MethodView):
    """
    Class with Methods For  Updating Specific Order Status
    """
    orderlistv1 = [{"order_id" : 1,
                    "order_name" : "packageOne", "quantity" : 3,
                    "payment_mode" : "Mobile Money",
                    "order_status" : "Completed"}, {"order_id" : 2,
                                                    "order_name" : "packageTwo",
                                                    "quantity" : 7,
                                                    "payment_mode" : "Cash On Delivery",
                                                    "order_status" : "Accepted"}]

    def update_orderv1(self, order_id):
        """
         Method For Updating Order Status.
        """
        for orderv1 in self.orderlistv1:
            if orderv1['order_id'] == order_id:
                order_json = request.get_json()
                orderv1['order_status'] = order_json['order_status']
                return jsonify({'Updated Order' : orderv1})
                