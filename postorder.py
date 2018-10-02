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
    
