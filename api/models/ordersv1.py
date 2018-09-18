"""
Module handling requsts made
on the API end points for Version1 Orders.
"""
from flask import jsonify, request
from flask.views import MethodView
class Ordersv1Handler(MethodView):
    """
    Class with Methods For  Handling Requests
    made on the API end point for version1 Orders.
    Control is Derived from OrderViews class
    """
    orderlistv1 = [{"order_id" : 1,
                    "order_name" : "packageOne",
                    "quantity" : 3,
                    "payment_mode" :"Mobile Money",
                    "order_status" : "Completed"}, {"order_id" : 2,
                                                    "order_name" : "packageTwo",
                                                    "quantity" : 7,
                                                    "payment_mode" : "Cash On Delivery",
                                                    "order_status" : "Accepted"}]


    requests = []
    def return_all_orders(self):
        """
        Method For Returning All Available Orders of Version 1
        """
        return jsonify({"message": "Successfully Retrieved Available Orders."
                                   , "orderlistv1": [self.orderlistv1]})
    def return_specific_order(self, order_id):
        """
        The Method Returns a Specific Order as to Enteredid
        """
        specific_order = [order for order in self.orderlistv1 if order['order_id'] == order_id]
        return jsonify({'Searched Order' : specific_order[0]})
    def post_orderv1(self):
        """
         A method for Posting a New Order of Version 1.
        """
        order = {'order_id' : request.json['order_id'],
                 'order_name' : request.json['order_name'],
                 'quantity' : request.json['quantity'],
                 'payment_mode' : request.json['payment_mode'],
                 'order_status' : request.json['order_status']}
        self.orderlistv1.append(order)
        return jsonify({'Added Order' : order})
    def update_orderv1(self, order_id):
        """
         A method for updating an order of version 1.
        """
        for orderv1 in self.orderlistv1:
            if orderv1['order_id'] == order_id:
                order_json = request.get_json()
                orderv1['order_status'] = order_json['order_status']
                return jsonify({'Updated Order' : orderv1})
                     