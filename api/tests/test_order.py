"""
Module For Testing Method Used To Return All Orders
"""
from api import APP

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client

def test_get_all_orders():
    """
     Testing a route for getting all the available orders
    """
    my_result = ROUTE_CLIENT().get('/api/v1/orders')

    assert my_result.status_code == 200
