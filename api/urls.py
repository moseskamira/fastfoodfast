"""
This module handels requests to urls.
"""
from api.views import OrderViews

class Urls():
    """
   Class to generate urls
    """
    @staticmethod
    def generate_url(app):
        """
         For Generating urls On The App
        """
        order_view = OrderViews.as_view('order_api')
        app.add_url_rule('/api/v1/orders', defaults={'order_id': None},
                         view_func=order_view, methods=['GET',])
        app.add_url_rule('/api/v1/orders/<int:order_id>', view_func=order_view,
                         methods=['GET', 'PUT',])

        app.add_url_rule('/api/v1/orders',
                         view_func=order_view, methods=['POST',])
     