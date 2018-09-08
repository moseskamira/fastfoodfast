"""
Module For Getting Specific Order by Id
"""
from flask import jsonify
from flask.views import MethodView
class Ordersv1Handler(MethodView):
    """
    Class Containing Method For Returning Specific Order
    """
    orderlistv1 = [{"order_id" : 1,
                    "order_name" : "packageOne", "quantity" : 3,
                    "payment_mode" : "Mobile Money",
                    "order_status" : "Completed"}, {"order_id" : 2,
                                                    "order_name" : "packageTwo",
                                                    "quantity" : 7,
                                                    "payment_mode" : "Cash On Delivery",
                                                    "order_status" : "Accepted"}]

    def return_specific_order(self, order_id):
        """
        The Method Returns a Specific Order as to Entered id
        """
        specific_order = [order for order in self.orderlistv1 if order['order_id'] == order_id]
        return jsonify({'Searched Order' : specific_order[0]})
