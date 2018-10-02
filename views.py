def get(self, order_id):
        """
        Returns All Orders if Id Not Set
        Returns Specific Order If Id Is Set
        """
        header = request.headers.get('Authorization')
        token = header.split()[1]
        if not token:
            return jsonify({"message": "Token Missing"}), 401

        decoded = self.user_object.decode_token(token)
        if isinstance(decoded, str):
            return self.user_object.decode_failure(decoded)
        if self.user_object.check_login_status(decoded):
            if not order_id:
                request_sql = """SELECT * FROM "order" """
            
                sql_data = (decoded)
                return self.orders_handler.return_all_orders(request_sql, sql_data)
            return self.orders_handler.return_single_order(order_id)
        return jsonify({"message": "Please login"}), 401
    
