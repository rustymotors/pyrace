from uuid import uuid4
from django.http import HttpResponse, HttpResponseBadRequest
from pyrace.shared.logging import getLogger

from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the login index.")

def login(request):
    logger = getLogger('authlogin.views.login')
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    
    if username is None or password is None:
        logger.error("Missing username or password")
        return HttpResponse("reasoncode=INV-200\nreasontext=Unable to login\nreasonurl=https://rusty-motors.com", content_type='text/plain')
    
    print(f"Login attempt: {username} / {password}")
    
    try:
        user = User.objects.get(username=username, password=password)
        token = uuid4()
        logger.info(f"User {user.username} logged in with token {token}")
        return HttpResponse("Valid=TRUE\nTicket=%s" % token, content_type='text/plain')
    except User.DoesNotExist:    
        logger.error(f"User {username} not found")
        return HttpResponse("reasoncode=INV-200\nreasontext=Unable to login\nreasonurl=https://rusty-motors.com", content_type='text/plain')
    
def shardList(request):
    return HttpResponse("ShardList")