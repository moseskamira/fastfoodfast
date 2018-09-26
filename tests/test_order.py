"""
Cide For Performing Various Tests On The App
"""
from flask import json
from api import APP

MYAPP = APP
ROUTE_CLIENT = MYAPP.test_client


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
                                    content_type="application/json",
                                    data=json.dumps(
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
                                   content_type="application/json",
                                   data=json.dumps(
                                       {
                                           "order_id": 2,
                                           "order_name": "packageTwo",
                                           "quantity": 7,
                                           "payment_mode": "Cash On Delivery",
                                           "order_status": "Completed"
                                       })
                                   )
    assert my_result.status_code == 200


def test_error_hander_returns_json():
    """
    The API Returns JSON Message When a Wrong Endpoint is Hit By User
    """
    response = ROUTE_CLIENT().get('/api/v1/orders/hi')
    assert response.status_code == 404


def test_if_data_posted_is_in_form_of_json():
    """
    function to test if data posted to the place order API is in form of Json
    """
    response = ROUTE_CLIENT().post(
        '/api/v1/orders', content_type='application/json',
        data=json.dumps(
            {
                "orders": [
                    {
                        "order_id": 8,
                        "order__name": "Package One",
                        "quantity": 5,
                        "payment_mode": "Mobile Money",
                        "order_status": "Accepted"
                    }
                ]
            }
        )
    )
    assert response.status_code == 200
    load_result_data = json.loads(response.data)
    assert 'orders' in load_result_data
    assert load_result_data['orders'][0]['order_id'] == 8
    assert load_result_data['orders'][0]['order_name'] == "Package One"
    assert load_result_data['orders'][0]['quantity'] == 5
    assert load_result_data['orders'][0]['payment_mode'] == "Mobile Money"
    assert load_result_data['order_status'] == "Accepted"
