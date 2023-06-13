from django.shortcuts import render


def login(request):
    
    context = {}
    
    return render(request, 'auth/login.html', context)

def register(request):
    
    context = {}
    
    return render(request, 'auth/register.html', context)

def forgot_password(request):
    
    context = {}
    
    return render(request, 'auth/forgot-password.html', context)

def new_password(request):
    
    context = {}
    
    return render(request, 'auth/new-password.html', context)