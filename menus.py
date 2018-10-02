def post_menu(self ):
        """
        Method To Save Menu Items To Menu
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
                      
