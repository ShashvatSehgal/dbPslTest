from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .middlewares import auth
# Create your views here.
@never_cache
@auth
def homePage(request):
    user = request.user
    alert_message = request.session.pop("alert_message", None)  # Retrieve & clear session message
    alert_type = request.session.pop("alert_type", None)
    return render(request,'homePage/home.html',{'title':'Home-page','user':user,
                                                'alert_message': alert_message,
                                                "alert_type": alert_type})