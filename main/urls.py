from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.Home,name="Home"),
    path("404/",views.Custom404,name="Custom404"),

]
