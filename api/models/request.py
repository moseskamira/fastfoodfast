"""
This module is a request model with its attributes
"""


class Request():
    """
    This class represents a Request entity
    """
    def __init__(self, *args):
        self.request_id = args[0]
        self.order_id = args[1]
        self.order_name = args[2]
        self.quantity = args[3]
        self.payment_mode = args[4]
        self.order_status = args[5]
