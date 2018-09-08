"""
Module For Testing Method For Getting Specific Order
"""
from api import APP

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client

def test_get_specific_order():
    """
     Testing a Route for getting a specific order
    """
    my_result = ROUTE_CLIENT().get('/api/v1/orders/1')

    assert my_result.status_code == 200
