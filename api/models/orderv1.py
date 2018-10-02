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
        self.quantity = args[1]
        self.totalamount = args[2]
        self.payment_mode = args[3]
        self.order_status = args[4]
        if len(args) > 5:
            self.order_id = args[5]
        else:
            self.order_id = None

    def save_order(self):
        """
        Method For Saving Order
        """

        order_sql = """INSERT INTO "order"(user_id, quantity, totalamount, 
            payment_mode, order_status)
        VALUES((%s), %s, %s, %s, %s);"""
        order_data = (
            self.user_id, self.quantity,
            self.totalamount, self.payment_mode,
            self.order_status
            )
        DbTransaction.save(order_sql, order_data)

    def get_order_information(self):
        """
        Method Returns Order Details.
        """

        return {
            "user_id": self.user_id,
            "Quantity": self.quantity,
            "Total Amount": self.totalamount,
            "Payment Mode": self.payment_mode,
            "Order Status": self.order_status
        }

    def check_order_existance(self):
        """
        Method For Checking Whether Order Exists Already.
        """
        sql = """SELECT "user_id", "quantity", "totalamount", "payment_mode",
        "order_status" FROM "order" WHERE "user_id" = %s;"""
        order_data = (self.user_id, self.quantity, self.totalamount, self.payment_mode,
                    self.order_status)
        order = DbTransaction.fetch_one(sql, order_data)
        if order is None:
            return {"status": "Success", "Message": "Order Does Not Exists"}
        return {"status": "fFailure", "Message": "Order Already Exists"}
