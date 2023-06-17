from datetime import timedelta
from django.utils import timezone
import json
import secrets
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.files.storage import default_storage
from django.urls import reverse
from Auth.mail import send_html_email
from Auth.views import anonymous_required


User = get_user_model()


@login_required
def default(request):

    context = {}

    return render(request, 'app/default.html', context)


@login_required
def teachers(request):
    errors, exist = [], False

    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_teacher = bool(request.POST.get('is_teacher'))
        is_staff = bool(request.POST.get('is_staff'))
        _method = request.POST.get('method')

        avatar = request.FILES.get('avatar')

        if _method == 'POST':

            if email or first_name or last_name:
                if User.objects.filter(email=email).exists():
                    exist = True
                    errors.append("Un utilisateur existe déjà avec cet email")

                if avatar and not exist:
                    file_extension = avatar.name.split('.')[-1]
                    avatar_name = f'{first_name}-{last_name}-{uuid.uuid4().hex}.{file_extension}'

                    file_path = f'avatars/{avatar_name}'
                    default_storage.save(file_path, avatar)
            else:
                errors.append("Veuillez remplir tous les champs obligatoires")

            if not exist:
                created_by = User.objects.get(id=request.user.id)
                
                token = secrets.token_urlsafe(32)
                reset_link = request.build_absolute_uri(
                    reverse('password.new', args=[token]))

                expire_at = 2
                
                user = {
                    'first_name': first_name,
                    'last_name': last_name
                }

                if send_html_email(
                    'Activation de compte WebP2MS',
                    'mails/new-password.html',
                    {'to': user, 'reset_link': reset_link, 'expire': expire_at},
                    [email]
                ):
                
                    User.objects.create(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        is_teacher=is_teacher,
                        is_staff=is_staff,
                        created_by=created_by,
                        avatar=file_path if avatar else None,
                        reset_token=token,
                        reset_token_expiration = timezone.now() + timedelta(hours=expire_at)
                    )

        elif _method in ['PUT', 'PATCH', 'UPDATE']:
            user_id = request.POST.get('user_id')
            user = User.objects.get(id=user_id)

            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            is_teacher = bool(request.POST.get('is_teacher'))
            is_staff = bool(request.POST.get('is_staff'))

            avatar = request.FILES.get('avatar')

            if email and first_name and last_name:
                if User.objects.filter(email=email).exclude(id=user_id).exists():
                    exist = True
                    errors.append("Un utilisateur existe déjà avec cet email")

                if avatar:
                    file_extension = avatar.name.split('.')[-1]
                    avatar_name = f'{first_name}-{last_name}-{uuid.uuid4().hex}.{file_extension}'

                    file_path = f'avatars/{avatar_name}'
                    default_storage.save(file_path, avatar)
                    user.avatar = file_path

                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.is_teacher = is_teacher
                user.is_staff = is_staff
                user.save()

        else:
            errors.append("Veuillez remplir tous les champs obligatoires")

    context = {
        'users': User.objects.filter(Q(is_teacher=True) | Q(is_staff=True)),
        'errors': errors
    }

    return render(request, 'app/teachers.html', context)


@login_required
def cours(request):

    context = {}

    return render(request, 'app/courses.html', context)


@login_required
def salles(request):

    context = {}

    return render(request, 'app/classrooms.html', context)


@login_required
def shedules(request):

    context = {}

    return render(request, 'app/shedules.html', context)


@login_required
def aides(request):

    context = {}

    return render(request, 'app/helps.html', context)

@csrf_exempt
@login_required
def ajax_delete_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('user_id')

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                user.delete()
                return JsonResponse({'success': 'User deleted successfully'})
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=400)
        else:
            return JsonResponse({'error': 'Missing user_id'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)