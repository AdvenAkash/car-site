from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('new', views.register),
    path('display', views.display),
    path('search',views.search),
    path('delete',views.delete),
]