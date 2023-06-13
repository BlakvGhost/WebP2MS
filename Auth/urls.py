from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgot-password', views.forgot_password, name='password.forgot'),
    path('new-password', views.new_password, name='password.new'),
]
