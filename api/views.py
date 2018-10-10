"""
Module Provides Responses url Requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from api.models.orders import OrdersHandler
from api.models.menus import MenuModel
from api.models.user import User
from api.models.admin import Admin


class OrderViews(MethodView):
    """
    Class Contains Methods Responding To Various url EndPoints.
    """
    orders_handler = OrdersHandler()

    user_object = User()
    admin_object = Admin()
    
    def post(self):
        """"
        Method Handles Order Posting
        """
        token = request.headers.get('Authorization')
        # token = header.split()[1]
        if not token:
            return jsonify({"message": "Token Missing"}), 401

        decoded = self.user_object.decode_token(token)
        print(decoded)
        
        if isinstance(decoded, str):
            return self.user_object.decode_failure(decoded)
        if self.user_object.check_login_status(decoded):
            if not request or not request.json:
                return jsonify({"status_code": 400, "data": str(request.data),
                                 "error_message": "Content Not JSON"}), 400
            return self.orders_handler.post_order(decoded)
        return jsonify({"message": "Please login"}), 401

    def get(self, order_id):
        """
        Returns All Orders if Id Not Set
        Returns Specific Order If Id Is Set
        """
        token = request.headers.get('Authorization')
        # token = header.split()[1]
        if not token:
            return jsonify({"message": "Token Missing"}), 401

        decoded = self.user_object.decode_token(token)
        if isinstance(decoded, str):
            return self.user_object.decode_failure(decoded)
        if self.user_object.check_login_status(decoded):
            if not order_id:
                request_sql = """SELECT * FROM "order" ORDER BY order_id DESC """
            
                sql_data = (decoded)
                return self.orders_handler.return_all_orders(request_sql, sql_data)
            return self.orders_handler.return_single_order(order_id)
        return jsonify({"message": "Please login"}), 401
    
    def put(self, order_id ):
        """
        Method To Update Order Status
        """
        token = request.headers.get('Authorization')
        # token = header.split()[1]
        if not token:
            return jsonify({"message": "Token Missing"}), 401

        decoded = self.admin_object.decode_token(token)
        if isinstance(decoded, str):
            return self.admin_object.decode_failure(decoded)
        if self.admin_object.check_login_status(decoded):
            if order_id:
                return self.orders_handler.update_order(order_id)
            return jsonify({"message": "Please login"}), 401
    

class MenuView(MethodView):
    """
    Class Handling url Endpoints For Menu.
    """
    menu_model = MenuModel()

    admin_object = Admin()
    user_object = User()

    def post(self):
         """
         Method To Post Menu.
         """
         token = request.headers.get('Authorization')
        #  token = header.split()[1]
         
         if not token:
             return jsonify({"message": "Token Missing"}), 401

         decoded = self.user_object.decode_token(token)
         print(decoded)
         if isinstance(decoded, str):
             return self.user_object.decode_failure(decoded)
         if self.user_object.check_login_status(decoded):
             if not request or not request.json:
                 return jsonify({"status_code": 400, "data": str(request.data),
                                 "error_message": "content not JSON"}), 400
             return self.menu_model.post_menu(decoded)
         return jsonify({"message": "Please login"}), 401

    def get(self):
        """
        Method For Retrieving All Items On Menu
        """
        request_sql = """SELECT * FROM "menu" ORDER BY item_id ASC"""
       
        return self.menu_model.return_menu(request_sql)
       
        