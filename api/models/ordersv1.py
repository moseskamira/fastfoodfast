"""
Module Handling Create Order Requst.
"""
from flask import jsonify, request
from flask.views import MethodView
class Ordersv1Handler(MethodView):
    """
    Class with Methods For  Handling Create Order Request
    """
    orderlistv1 = [{"order_id" : 1,
                    "order_name" : "packageOne", "quantity" : 3,
                    "payment_mode" : "Mobile Money",
                    "order_status" : "Completed"}, {"order_id" : 2,
                                                    "order_name" : "packageTwo",
                                                    "quantity" : 7,
                                                    "payment_mode" : "Cash On Delivery",
                                                    "order_status" : "Accepted"}]


    requests = []
    def post_orderv1(self):
        """
         Method For Creating/ Posting a New Order.
        """
        order = {'order_id' : request.json['order_id'],
                 'order_name' : request.json['order_name'],
                 'quantity' : request.json['quantity'],
                 'payment_mode' : request.json['payment_mode'],
                 'order_status' : request.json['order_status']}
        self.orderlistv1.append(order)
        return jsonify({'Added Order' : order})
