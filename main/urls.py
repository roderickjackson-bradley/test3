from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wish_list, name='wish_list'),
  ]
