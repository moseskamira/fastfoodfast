"""
Cide For Performing Various Tests On The App
"""
from flask import json
from api import APP

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client

def test_put_order():
    """
   Testing the route for updating an rder
    """
    my_result = ROUTE_CLIENT().put('/api/v1/orders/1',
                                   content_type="application/json", data=json.dumps(
                                       {
                                           "order_id" : 2,
                                           "order_name" : "packageTwo",
                                           "quantity": 7,
                                           "payment_mode" : "Cash On Delivery",
                                           "order_status" : "Completed"
                                       }))
    assert my_result.status_code == 200
