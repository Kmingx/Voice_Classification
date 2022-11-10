from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.indexpage),
    path('menulist/', views.menuList),
]