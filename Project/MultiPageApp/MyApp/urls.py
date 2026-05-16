from django.contrib import admin
from django.urls import path,include
from MyApp import views

urlpatterns = [
     path('',views.index),
  
]