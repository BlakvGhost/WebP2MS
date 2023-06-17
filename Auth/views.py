from datetime import timedelta
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import secrets
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .models import MyUser as User
from .mail import send_html_email


def anonymous_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('teachers')
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
def new_password(request, token):

    context = {'token': token}

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
                    user = User.objects.create_user(
                        email=email, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()

                    user = authenticate(
                        request, email=email, password=password)
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

                token = secrets.token_urlsafe(32)
                reset_link = request.build_absolute_uri(
                    reverse('password.new', args=[token]))

                expire_at = 2
                user.reset_token = token
                user.reset_token_expiration = timezone.now() + timedelta(hours=expire_at)
                user.save()

                if send_html_email(
                    'Réinitialisation de votre mot de passe',
                    'mails/forgot-password.html',
                    {'to': user, 'reset_link': reset_link, 'expire': expire_at},
                    [email]
                ):
                    return JsonResponse({'success': 'Instructions de réinitialisation du mot de passe envoyées à votre adresse e-mail'}, status=201)
                else:
                    return JsonResponse({'error': 'Impossible d\'envoyer l\'e-mail'}, status=400)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Aucun utilisateur avec cet e-mail'}, status=404)
        else:
            return JsonResponse({'error': 'E-mail manquant'}, status=400)
    else:
        return JsonResponse({'error': 'Méthode HTTP invalide'}, status=400)


@csrf_exempt
@anonymous_required
def ajax_new_password(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        password = data.get('password')
        confirm_password = data.get('confirm_password')
        token = data.get('token')

        if password and confirm_password and token:
            if password == confirm_password:
                try:
                    user = User.objects.get(reset_token=token)
                    if user.is_reset_token_valid(token) and not user.is_reset_token_expired():
                        user.set_password(password)
                        user.reset_token = None
                        user.reset_token_expiration = None
                        user.save()
                        return JsonResponse({'success': 'Réinitialisation du mot de passe réussie'}, status=201)
                    else:
                        return JsonResponse({'error': 'Jeton invalide ou expiré'}, status=400)
                except User.DoesNotExist:
                    return JsonResponse({'error': 'Jeton invalide ou expiré'}, status=400)
            else:
                return JsonResponse({'error': 'Les mots de passe ne correspondent pas'}, status=400)
        else:
            return JsonResponse({'error': 'Mot de passe, confirmation de mot de passe ou jeton manquant'}, status=400)
    else:
        return JsonResponse({'error': 'Méthode HTTP invalide'}, status=400)
