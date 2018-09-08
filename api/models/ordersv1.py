"""
Module Handling Requst For Returning All Orders
"""
from flask import jsonify
from flask.views import MethodView
class Ordersv1Handler(MethodView):
    """
    Class with Method For  Returning All Available Orders
    """
    orderlistv1 = [{"order_id" : 1,
                    "order_name" : "packageOne",
                    "quantity" : 3,
                    "payment_mode" : "Mobile Money",
                    "order_status" : "Completed"}, {"order_id" : 2,
                                                    "order_name" : "packageTwo",
                                                    "quantity" : 7, "payment_mode" :
                                                    "Cash On Delivery",
                                                    "order_status" : "Accepted"}]
    def return_all_orders(self):
        """
        Method For Returning All Available Orders
        """
        return jsonify({"message": "Successfully Retrieved Available Orders."
                                   , "orderlistv1": [self.orderlistv1]})
