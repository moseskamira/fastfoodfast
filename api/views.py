"""
Module Provides Responses url Requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from api.models.orders import OrdersHandler
from api.models.menus import MenuModel
from api.models.user import User


class OrderViews(MethodView):
    """
    Class Contains Methods Responding To Various url EndPoints.
    """
    orders_handler = OrdersHandler()

    user_object = User()
  
    
    def post(self):
        """"
        Method Handles Order Posting
        """
        
        token = request.headers.get('x-access-token')

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
        token = request.headers.get('x-access-token')
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
    
class MenuView(MethodView):
    """
    Class Handling url Endpoints For Menu.
    """
    menu_model = MenuModel()

   
    user_object = User()

    def post(self):
         """
         Method To Post Menu.
         """
         token = request.headers.get('x-access-token')
         
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

class OrderHistory(MethodView):
    """
    Class Contains Method Responding To Various url EndPoints
    For specific order fetching.
    """
    orders_handler = OrdersHandler()

    user_object = User()

    def get(self):
        """
        This Method Gets Orders Made By Specific User
        """
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({"message": "Token Missing"}), 401

        decoded = self.user_object.decode_token(token)

        if isinstance(decoded, str):
            return self.user_object.decode_failure(decoded)
        if self.user_object.check_login_status(decoded):
            order_sql = """SELECT *FROM "order" WHERE user_id = %s """
            sql_data = decoded
            
            return self.orders_handler.return_orders_history(order_sql, sql_data)
        return jsonify({"message": "Please login"}), 401
       