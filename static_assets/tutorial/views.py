# from pyramid.view import view_config
#
#
# # First view, available at http://localhost:6543/
# @view_config(route_name='home', renderer='home.pt')
# def home(request):
#     return {'name': 'Home View'}
#
#
# # /howdy
# @view_config(route_name='hello', renderer='home.pt')
# def hello(request):
#     return {'name': 'Hello View'}


from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'name': 'static View'}

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'static View'}