import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .models import MyUser as User
from .mail import send_html_email

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

@csrf_exempt
@anonymous_required
def ajax_login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                user_login(request, user)
                return JsonResponse({'success': 'User logged in successfully'})
            else:
                return JsonResponse({'error': 'Email ou Mot de Passe Incorrecte'}, status=401)
        else:
            return JsonResponse({'error': 'Email ou Mot de Passe nom rempli'}, status=400)
    else:
        return JsonResponse({'error': 'Methode HTTP invalid'}, status=400)
    
@csrf_exempt
@anonymous_required
def ajax_register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        password_confirm = data.get('confirm_password')

        if email and password and first_name and last_name:
            if password == password_confirm:
                try:
                    user = User.objects.get(email=email)
                    return JsonResponse({'error': 'User with this email already exists'}, status=400)
                except User.DoesNotExist:
                    user = User.objects.create_user(email=email, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()

                    user = authenticate(request, email=email, password=password)
                    if user is not None:
                        user_login(request, user)
                        return JsonResponse({'success': 'User registered and logged in successfully'})
                    else:
                        return JsonResponse({'error': 'Email or password incorrect'}, status=401)
            else:
                return JsonResponse({'error': 'Passwords do not match'}, status=400)
        else:
            return JsonResponse({'error': 'Missing email, password, first name, or last name'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)



@csrf_exempt
@anonymous_required
def ajax_forgot_password(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        email = data.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                
                new_password = User.objects.make_random_password()
                
                user.set_password(new_password)
                user.save()
                
                if send_html_email(
                    'Réinitialisation de votre mot de passe',
                    'mails/forgot-password.html',
                    {'password': new_password},
                    [email]
                ): 
                
                    return JsonResponse({'success': 'Password reset instructions sent to your email'}, status=201)
                return JsonResponse({'error': 'Email not sent'}, status=400)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User with this email does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'Missing email'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)
