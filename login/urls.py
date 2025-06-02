from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='login'),
    path('logout/',views.user_logout, name='logout'),
]
