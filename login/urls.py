from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='login'),
    path('',views.user_logout, name='logout'),
]
