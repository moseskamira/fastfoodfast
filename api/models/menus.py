"""
Module For Handling Menu Endpoints.
"""
from flask import jsonify, request
from api.models.db_transaction import DbTransaction
from api.models.orders import OrdersHandler
from api.models.error_messages import ErrorMessage
from api.models.menu import Menu


class MenuModel(object):
    """
    This class contains methods that handle specific
    Menu Queries.
    """

    error_message = ErrorMessage()

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

    def post_menu(self ):
        """
        Method To Save Menu Items
        """
        keys = ("item_category", "item_name", "price")
        if not set(keys).issubset(set(request.json)):
            return self.error_message.request_missing_fields()
        request_condition = [
            request.json["item_category"].strip(),
            request.json["item_name"].strip(),
            request.json["price"]
            ]
        if not all(request_condition):
            return self.error_message.fields_missing_information(request.json)
        
        item_category = request.json['item_category']
        item_name = request.json['item_name']
        price = request.json['price']
        
        menu = Menu(item_category, item_name, price)
        menu_existance = menu.check_menu_existance()
        if menu_existance["status"] == "failure":
            return jsonify({"message": menu_existance["message"]}), 400

        menu.save_menu()
        return jsonify({"status_code": 201, "Menu": menu.get_menu_information(),
                        "Message": "Menu Item Added Successfully"}), 201
                      
