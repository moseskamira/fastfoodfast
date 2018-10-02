def return_single_order(self, order_id):
        """
        Method To Return Single Order By Admin
        """
        request_sql = """ SELECT * FROM "order" WHERE order_id = {}""".format(order_id)
        order_turple = DbTransaction.fetch_one(request_sql, order_id)

        if order_turple is not None:
            order_id = order_turple[0]
            user_id = order_turple[1]
            quantity = order_turple[2]
            totalamount = order_turple[3]
            payment_mode = order_turple[4]
            order_status = order_turple[5]
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
