from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout as user_logout


def anonymous_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view_func(request, *args, **kwargs)
    return wrapped_view

@anonymous_required
def login(request):
    
    context = {}
    
    return render(request, 'auth/login.html', context)

@anonymous_required
def register(request):
    
    context = {}
    
    return render(request, 'auth/register.html', context)

@anonymous_required
def forgot_password(request):
    
    context = {}
    
    return render(request, 'auth/forgot-password.html', context)

@anonymous_required
def new_password(request):
    
    context = {}
    
    return render(request, 'auth/new-password.html', context)

@login_required
def logout(request):
    
    user_logout(request)
    return redirect('login')

@anonymous_required
def ajax_login(request):
    
    context = {}
    return JsonResponse(context)