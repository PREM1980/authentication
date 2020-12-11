from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
    )

from pyramid.view import (
    view_config,
    view_defaults
    )

from .security import (
    USERS,
    check_password
)

import logging
log = logging.getLogger(__name__)

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        log.debug('logged_in - {0}'.format(self.logged_in))

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
        # print_requests(self.request)
        return {'name': 'Hello View'}

    @view_config(route_name='login', renderer='login.pt')
    def login(self):
        # print_requests(self.request)
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        log.debug('login_url - {0}'.format(login_url))
        log.debug('referrer - {0}'.format(referrer))
        if referrer == login_url:
            referrer = '/'  # never use login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        log.debug('came_from - {0}'.format(request.params.get('came_from')))
        log.debug('request.application_url - {0}'.format(request.application_url))
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            log.debug('users.get start')
            hashed_pw = USERS.get(login)
            log.debug('users.get complete')
            if hashed_pw and check_password(password, hashed_pw):
                log.debug('remember')
                headers = remember(request, login)
                log.debug('remember done')
                # log.debug('headers - {0}'.format(headers))
                return HTTPFound(location=came_from,
                                 headers=headers)
            message = 'Failed login'

        return dict(
            name='Login',
            message=message,
            url=request.application_url + '/login',
            came_from=came_from,
            login=login,
            password=password,)


    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('home')
        return HTTPFound(location=url,
                         headers=headers)


# def print_requests(request):
#     log.debug('request.get - {0}'.format(request.GET))
#     log.debug('request.post - {0}'.format(request.POST))
#     log.debug('request.params - {0}'.format(request.params))
#     log.debug('request.body - {0}'.format(request.body))
#     log.debug('request.headers - {0}'.format(request.headers))
#     # log.debug('request.headers -', dir(request.headers))
#     log.debug('request.cookies -  {0}'.format(request.cookies))
#
#     for each in request.headers.items():  # cant we see the nih_cn and sm_user in the header
#         log.debug('headers item -  {0}'.format(each))
#
#     for each in request.params.iteritems():
#         log.debug('params item - {0}'.format(each))