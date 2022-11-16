from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index), #DB데이터
    path('', views.indexpage), #input 페이지
    path('menulist/', views.menuList, name='index'), # output페이지
]