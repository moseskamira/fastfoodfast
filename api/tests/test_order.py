"""
Module Used To Test Method For Creating Order
"""
from flask import json
from api import APP

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client

def test_post_order():
    """
   Testing the route for updating an rder
    """
    my_result = ROUTE_CLIENT().post('/api/v1/orders',
                                    content_type="application/json", data=json.dumps(
                                        {
                                            "order_id": 2,
                                            "order_name": "packageTwo",
                                            "payment_mode": "Cash On Delivery",
                                            "quantity": 7,
                                            "order_status" : "Completed"
                                        })
                                    )
    assert my_result.status_code == 200
