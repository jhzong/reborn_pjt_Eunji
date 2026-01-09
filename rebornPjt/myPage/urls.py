from django.urls import path
from . import views

app_name='mypage'
urlpatterns = [
    path('My_main/', views.My_main, name='My_main'),
    
]