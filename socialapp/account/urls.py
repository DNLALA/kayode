from re import template
from telnetlib import LOGOUT
from unicodedata import name
from django.contrib import admin
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views
from account import views
from django.contrib.auth import get_user_model

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sigup/', views.signup.as_view(), name='signup')
]
