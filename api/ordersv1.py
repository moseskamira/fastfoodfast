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
    orderlistv1 = []

    def return_all_orders(self):
        """
        Method For Returning All Available Orders of Version 1
        """
        return jsonify({"message": "Available Orders.",
                        "orderlistv1": self.orderlistv1})

    def return_specific_order(self, order_id):
        """
        The Method Returns a Specific Order as to Enteredid
        """
        for order in self.orderlistv1:
            if order['order_id'] == order_id:
                return jsonify({"Status code": 200, "Order": order,
                                "message": "Order Successfully Fetched"})
        return jsonify({"Error Message":
                        "No Order Found That Match Specified Id"})

    def post_orderv1(self):
        """
         A method for Posting a New Order of Version 1.
        """
        requiredkeys = ("order_name", "quantity", "payment_mode",
                        "order_status")
        if not set(requiredkeys).issubset(set(request.json)):
            return self.request_missing_fields()
        order_request = [
            request.json["order_name"],
            request.json["quantity"],
            request.json["payment_mode"],
            request.json["order_status"]
        ]
        if not all(order_request):
            return self.fields_missing_info()
        if not isinstance(request.json['quantity'], int):
            return jsonify({'Error': 'Please Enter Integer Value'})
        order = {'order_id': len(self.orderlistv1)+1,
                 'order_name': request.json['order_name'],
                 'quantity': request.json['quantity'],
                 'payment_mode': request.json['payment_mode'],
                 'order_status': request.json['order_status']}
        self.orderlistv1.append(order)
        return jsonify({'Added Order': order})

    def update_orderv1(self, order_id):
        """
         A method for updating an order of version 1.
        """
        for orderv1 in self.orderlistv1:
            if orderv1['order_id'] == order_id:
                order_json = request.get_json()
                orderv1['order_status'] = order_json['order_status']
                if not order_json['order_status']:
                    return jsonify({'Error': 'Enter Order Status'})
                return jsonify({'Updated Order': orderv1})
            return jsonify({"Message": "Order_Id Mismatch"})

    @staticmethod
    def request_missing_fields():
        """
        Method Returns JSON Response When Some Fields Are Missing
        """
        return jsonify({"Error_Message": "Some Fields Are Missing"}), 400

    @staticmethod
    def fields_missing_info():
        """
        Method Returns JSON Response When Some Fields Are Empty
        :return
        """
        return jsonify({"status_code": 400, "data": request.json,
                        "Error_Message": "Some Fields Are Empty"}), 400
