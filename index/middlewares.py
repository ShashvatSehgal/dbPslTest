from functools import wraps
from django.shortcuts import redirect

def auth(viewFunction):
    @wraps(viewFunction)
    def wrappedView(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return viewFunction(request, *args, **kwargs)
    return wrappedView
