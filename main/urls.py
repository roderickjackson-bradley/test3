from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.wish_list, name='wish_list'),
    path('new/', views.wish_create, name='wish_create'),
    path('edit/<int:pk>/', views.wish_update, name='wish_update'),
    path('delete/<int:pk>/', views.wish_delete, name='wish_delete'),

  ]