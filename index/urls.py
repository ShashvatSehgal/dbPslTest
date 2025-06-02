from django.urls import path,include
from . import views
urlpatterns = [
path('indexPage/', views.indexPage,name='index'),
]