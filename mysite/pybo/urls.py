from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.indexpage),
    path('menulist/', views.menuList, name='index'),
]