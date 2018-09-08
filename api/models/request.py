"""
This module is a request model with its attributes
"""
class Request(object):
    """
    This class represents a Request entity
    """
    def __init__(self, *args):
        self.request_id = args[0]
        self.order_id = args[1]
        self.order_name = args[2]
        self.quantity = args[3]
        