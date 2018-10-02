"""
This module handels requests to urls.
"""
from api.views import OrderViews, MenuView
from api.authentication.views import UserRegistration, UserLogin, UserLogout

class Urls(object):
    """
    Class to generate urls
    """
    @staticmethod
    def generate_url(app):
        """
         Generates urls on the app context
        :param: app: takes in the app variable
        :return: urls
        """
        order_view = OrderViews.as_view('order_api')
        app.add_url_rule('/api/v1/users/orders', defaults={'order_id': None},
                         view_func=order_view,
                         methods=['GET',])

        app.add_url_rule('/api/v1/users/orders', view_func=order_view, methods=['POST',])

        app.add_url_rule('/api/v1/auth/signup', view_func=UserRegistration.as_view('register_user'),
                         methods=["POST",])
        app.add_url_rule('/api/v1/auth/login', view_func=UserLogin.as_view('login_user'),
                         methods=["POST",])
        
        app.add_url_rule('/api/v1/users/logout',
                         view_func=UserLogout.as_view('logout_user'),
                         methods=["POST",])



        app.add_url_rule('/api/v1/admin/orders', defaults={'order_id': None},
                         view_func=order_view,
                         methods=['GET',])
        app.add_url_rule('/api/v1/admin/orders/<int:order_id>', view_func=order_view, methods=['GET',])

        
        app.add_url_rule('/api/v1/admin/menu', view_func=MenuView.as_view('post_menu'),
                         methods=["POST",])
        app.add_url_rule('/api/v1/menu', view_func=MenuView.as_view('get_menu'),
                         methods=["GET",])

        

      
