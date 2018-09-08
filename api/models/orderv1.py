"""
Module Describing An Order of Version 1
"""
class Orderv1(object):
    """
    Class Describing Order of Version 1 (orderv1)
    """
    def __init__(self, *args):
        self.order_id = args[0]
        self.order_name = args[1]
        self.quantity = args[2]
        self.payment_mode = args[3]
        self.order_status = args[4]
