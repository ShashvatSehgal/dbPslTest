from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .middlewares import auth
from django.http import JsonResponse
# Create your views here.
@never_cache
@auth
def homePage(request):
    print("User is_authenticated:", request.user.is_authenticated)
    user = request.user
    alert_message = request.session.pop("alert_message", None)  # Retrieve & clear session message
    alert_type = request.session.pop("alert_type", None)
    return render(request,'homePage/home.html',{'title':'Home-page','user':user,
                                                'alert_message': alert_message,
                                                "alert_type": alert_type})

@login_required
def session_check(request):
    return JsonResponse({'status': 'ok'})