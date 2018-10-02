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
