from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.home),
    path("index/",views.index),
    path("signup/",views.signup),
    path("login/",views.login,name="login"),
    
    
]
