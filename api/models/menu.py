"""
Menu Module With Attributes
"""
from api.models.db_transaction import DbTransaction


class Menu(object):
    """
    Class Represents Menu Entity
    """

    def __init__(self, item_category, item_name, item_price, item_id=None):
        self.item_category = item_category
        self.item_name = item_name
        self.item_price = item_price

    def save_menu(self, user):
        """
        Method Saves Menu.
        """

        menu_sql = """INSERT INTO "menu"(item_category, item_name, item_price, user_id)
            VALUES(%s, %s, %s, %s);"""
        menu_data = (self.item_category, self.item_name, self.item_price, user)
        DbTransaction.save(menu_sql, menu_data)

    def get_menu_information(self):
        """
        Method Returns Information of about Menu.
        """
        return {
            "item_category": self.item_category,
            "item_name": self.item_name,
            "price": self.item_price
        }

    def check_menu_existance(self):
        """
        Checks Existance of Menu.
        """
        check_sql = """SELECT "item_category", "item_name", "item_price" FROM "menu"
        WHERE "item_category" = %s AND "item_name" = %s"""
        menu_data = (self.item_category, self.item_name, self.item_price)
        menu_query = DbTransaction.fetch_one(check_sql, menu_data)
        if menu_query is None:
            return {"status": "success", "message": "Menu Does Not Exists"}
        return {"status": "failure", "message": "Menu Already Exists"}
