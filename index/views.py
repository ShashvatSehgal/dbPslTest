from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .middlewares import auth
# Create your views here.
@auth
@never_cache
def indexPage(request):
    return render(request,'index/indexPage.html')