from django.shortcuts import redirect


# *************** Authenticated  **************
def auth(viewFunction):
    def wrappedView(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return viewFunction(request,*args,**kwargs)
    return wrappedView
