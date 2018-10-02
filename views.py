class MenuView(MethodView):
    """
    Class Handling url Endpoints For Menu.
    """
    menu_model = MenuModel()

    user_object = User()

    def post(self):
         """
         Method To Edit Menu.
         """
         header = request.headers.get('Authorization')
         token = header.split()[1]
         print(token)
         if not token:
             return jsonify({"message": "Token Missing"}), 401

         decoded = self.user_object.decode_token(token)
         if isinstance(decoded, str):
             return self.user_object.decode_failure(decoded)
         if self.user_object.check_login_status(decoded):
             if not request or not request.json:
                 return jsonify({"status_code": 400, "data": str(request.data),
                                 "error_message": "content not JSON"}), 400
             return self.menu_model.post_menu()
         return jsonify({"message": "Please login"}), 401
