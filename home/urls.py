from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("quizhome", views.quizhome, name="quizhome"),
    path("login", views.handleLogin, name="handleLogin"),
    path("logout", views.handleLogout, name="handleLogout")
   
]
