def return_menu(self, sql_statement, data=None):
        """
        Method Returns All Items On Menu
        """
        sql = sql_statement
        requests_turple_list = []
        if  data is not None:
            requests_turple_list = DbTransaction.fetch_all(sql, data)
        else:
            requests_turple_list = DbTransaction.fetch_all(sql)

        request_list = []
        for request_tuple in requests_turple_list:
            request_dict = {
                "item_category": request_tuple[1],
                "item_id": request_tuple[0],
                "item_name": request_tuple[2],
                "price": request_tuple[3]
            }
            request_list.append(request_dict)
        return jsonify({"Message": "Menu Fetched Successfully",
                        "Available Menu": request_list})
