from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse
import re

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS+=[re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

PREVIEW_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'PREVIEW_URLS'):
    PREVIEW_URLS+=[re.compile(url) for url in settings.PREVIEW_URLS]

class LoginRequiredMiddleware:
    def __init__(self,get_response):
       self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request,'user')
        path=request.path_info.lstrip('/')

        #if not request.user.is_authenticated:
        #    if not any(url.match(path) for url in EXEMPT_URLS):
        #        return redirect(settings.LOGIN_URL)

        url_is_exempt= any(url.match(path) for url in EXEMPT_URLS)

        url_is_preview = any(url.match(path) for url in PREVIEW_URLS)

        if path==reverse('accounts:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt or url_is_preview:
            return None
        else:
            return redirect(settings.LOGIN_URL)

