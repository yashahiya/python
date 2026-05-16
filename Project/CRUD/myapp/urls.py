from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index),
    path("show/",views.show,name="show"),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),


]
