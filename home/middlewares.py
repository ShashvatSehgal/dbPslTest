from functools import wraps
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.cache import patch_cache_control

def auth(viewFunction):
    @wraps(viewFunction)
    def _wrappedView(request, *args, **kwargs):
        if not request.user.is_authenticated:
            request.session["alert_message"] = "Access denied. Please log in again."
            request.session["alert_type"] = "warning"
            return redirect('login')

        response = viewFunction(request, *args, **kwargs)
        patch_cache_control(response, no_cache=True, no_store=True, must_revalidate=True)
        return response
    return _wrappedView

class DisableClientSideCachingMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response

