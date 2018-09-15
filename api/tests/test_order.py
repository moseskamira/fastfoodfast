"""
Cide For Performing Various Tests On The App
"""
from flask import json
from api import APP

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client
CLIENT = MYAPP.test_client

def test_get_all_orders():
    """
     Testing a route for getting all the available orders
    """
    my_result = ROUTE_CLIENT().get('/api/v1/orders')

    assert my_result.status_code == 200
def test_get_specific_order():
    """
     Testing a Route for getting a specific order
    """
    my_result = ROUTE_CLIENT().get('/api/v1/orders/1')

    assert my_result.status_code == 200
def test_post_order():
    """
      Testing the route for posting an order
    """
    my_result = ROUTE_CLIENT().post('/api/v1/orders',
                                    content_type="application/json", data=json.dumps(
                                        {
                                            "order_id": 2,
                                            "order_name": "packageTwo",
                                            "quantity": 7,
                                            "payment_mode": "Cash On Delivery",
                                            "order_status": "Completed",
                                        }
                                        )
                                    )
    assert my_result.status_code == 200
def test_put_order():
    """
   Testing the route for updating an rder
    """
    my_result = ROUTE_CLIENT().put('/api/v1/orders/1',
                                   content_type="application/json", data=json.dumps(
                                       {
                                           "order_id": 2,
                                           "order_name" : "packageTwo",
                                           "quantity" : 7,
                                           "payment_mode" : "Cash On Delivery",
                                           "order_status" : "Completed"
                                       })
                                   )
    assert my_result.status_code == 200
    