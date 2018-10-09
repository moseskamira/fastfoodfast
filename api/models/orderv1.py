"""
Module For Order Model With Attributes
"""
from api.models.db_transaction import DbTransaction


class Order(object):
    """
    Class Representing Order Entity
    """

    def __init__(self, *args):
        self.user_id = args[0]
        self.order_name = args[1]
        self.quantity = args[2]
        self.total_amount = args[3]
        self.payment_mode = args[4]
        if len(args) > 5:
            self.order_id = args[5]
        else:
            self.order_id = None

    def save_order(self):
        """
        Method For Saving Order
        """

        order_sql = """INSERT INTO "order"(user_id, order_name, quantity, total_amount, 
            payment_mode)
        VALUES((%s), %s, %s, %s, %s);"""
        order_data = (
            self.user_id, self.order_name,
            self.quantity,
            self.total_amount,
            self.payment_mode
            )
        DbTransaction.save(order_sql, order_data)

    def get_order_information(self):
        """
        Method Returns Order Details.
        """

        return {
            "user_id": self.user_id,
            "order_name": self.order_name,
            "Quantity": self.quantity,
            "Total Amount": self.total_amount,
            "Payment Mode": self.payment_mode,
        }

    def check_order_existance(self):
        """
        Method For Checking Whether Order Exists Already.
        """
        sql = """SELECT "user_id", "quantity", "totalamount", "payment_mode",
        "order_status" FROM "order" WHERE "user_id" = %s;"""
        order_data = (self.user_id, self.order_name, self.quantity, self.total_amount, self.payment_mode)
        order = DbTransaction.fetch_one(sql, order_data)
        if order is None:
            return {"status": "Success", "Message": "Order Does Not Exists"}
        return {"status": "fFailure", "Message": "Order Already Exists"}
