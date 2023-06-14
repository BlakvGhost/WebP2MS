from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgot-password', views.forgot_password, name='password.forgot'),
    path('new-password', views.new_password, name='password.new'),
    path('logout', views.logout, name='logout'),
    
    #Ajax routes
    
    path('ajax-login', views.ajax_login, name="ajax.login"),
    path('ajax-register', views.ajax_register, name="ajax.register"),
    path('ajax-password.forgot', views.ajax_forgot_password, name="ajax.password.forgot"),
]
