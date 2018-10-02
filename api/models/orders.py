"""
Module For Handling Specific Requsts On
API End Points
"""
from flask import jsonify, request
from api.models.db_transaction import DbTransaction
from api.models.error_messages import ErrorMessage
from api.models.orderv1 import Order


class OrdersHandler:
    """
    Class Containing Methods For Handling Order
    """

    error_message = ErrorMessage()

    def return_all_orders(self, sql_statement, data=None):
        """
        Method For Returning All Available Orders
        """
        sql = sql_statement
        requests_turple_list = []
        if  data is not None:
            requests_turple_list = DbTransaction.fetch_all(sql)
        else:
            requests_turple_list = DbTransaction.fetch_all(sql, data)
            print(requests_turple_list)

        request_list = []
        for request_tuple in requests_turple_list:
            request_dict = {
                "order_id": request_tuple[0],
                "user_id": request_tuple[1],
                "quantity": request_tuple[2],
                "totalamount":  request_tuple[3],
                "payment_mode": request_tuple[4],
                "order_status":  request_tuple[5]
            }

            request_list.append(request_dict)
        return jsonify({"Message": "Order Successfully Fetched",
                        "orders": request_list})

    def return_single_order(self, order_id):
        """
        Method For Getting Single Order
        """
        request_sql = ("SELECT * FROM order WHERE order_id = %s", order_id)
        order_turple = DbTransaction.fetch_all(request_sql, (order_id))

        if order_turple is not None:
            user_id = order_turple[0]
            order_id = order_turple[2]
            quantity = order_turple[3]
            totalamount = order_turple[4]
            payment_mode = order_turple[5]
            order_status = order_turple[6]
            return jsonify({"Status code": 200, "Order Information": {
                 "user_id": user_id,
                "order_id": order_id,
                "quantity": quantity,
                "totalamount": totalamount,
                "payment_mode": payment_mode,
                "order_ststaus": order_status
            },
                            "message": "Order Fetched Successfully"})
        return self.error_message.no_order_available(order_id)

    def post_order(self, user_id):
        """
        Method For Saving Order
        """
        keys = ("quantity", "totalamount", "payment_mode", "order_status")
        if not set(keys).issubset(set(request.json)):
            return self.error_message.request_missing_fields()

        request_condition = [
            request.json["quantity"],
            request.json["totalamount"],
            request.json["payment_mode"].strip(),
            request.json["order_status"]
            ]
        print(request_condition)
        #request_condition.append(user_id)
        if not all(request_condition):
            return self.error_message.fields_missing_information(request.json)

        user = DbTransaction.fetch_one(
            """SELECT "user_id" FROM users WHERE "user_id" = %s""",
            (user_id, ))
        if user is None:
            return self.error_message.no_user_found_response("Order Not created", user_id)
        quantity = request.json['quantity']
        totalamount = request.json['totalamount']
        payment_mode = request.json['payment_mode']
        order_status = request.json['order_status']

        order = Order(user, quantity, totalamount,
                    payment_mode, order_status
                )
        order_existance = order.check_order_existance()
        if order_existance["status"] == "failure":
            return jsonify({"message": order_existance["message"]}), 400

        order.save_order()
        return jsonify({"status_code": 201, "order": order.get_order_information(),
                        "Message": "Order Added Successfully"}), 201
                        