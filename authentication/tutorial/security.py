import bcrypt

# from .views import print_requests

import logging
log = logging.getLogger(__name__)

def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')

def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf8')
    return bcrypt.checkpw(pw.encode('utf8'), expected_hash)


USERS = {'editor': hash_password('editor'),
         'viewer': hash_password('viewer')}
GROUPS = {'editor': ['group:editors']}


def groupfinder(userid, request):
    # print_requests(request)
    log.debug('groupfinder called userid - {0}'.format(userid))
    log.debug('GROUPS.get(userid, []) - {0}'.format(GROUPS.get(userid, [])))
    if userid in USERS:
        return GROUPS.get(userid, [])

# def print_requests(request):
#     log.debug('request.get - {0}'.format(request.GET))
#     log.debug('request.post - {0}'.format(request.POST))
#     log.debug('request.params - {0}'.format(request.params))
#     log.debug('request.body - {0}'.format(request.body))
#     log.debug('request.headers - {0}'.format(request.headers))
#     # log.debug('request.headers -{0}'.format(dir(request.headers)))
#     log.debug('request.cookies -  {0}'.format(request.cookies))
#
#     for each in request.headers.items():  # cant we see the nih_cn and sm_user in the header
#         log.debug('headers item -  {0}'.format(each))
#
#     for each in request.params.iteritems():
#         log.debug('params item - {0}'.format(each))