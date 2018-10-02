def get(self):
        """
        Method For Retrieving All Items On Menu
        """
        header = request.headers.get('Authorization')
        token = header.split()[1]
        if not token:
            return jsonify({"message": "Token Missing"}), 401

        decoded = self.user_object.decode_token(token)
        if isinstance(decoded, str):
            return self.user_object.decode_failure(decoded)
        if self.user_object.check_login_status(decoded):
            request_sql = """SELECT * FROM "menu" """
            sql_data = (decoded)
            return self.menu_model.return_menu(request_sql, sql_data)
        return jsonify({"message": "Please login"}), 401
