from datetime import timedelta
from django.utils import timezone
import json
import secrets
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.core.files.storage import default_storage
from django.urls import reverse
from Auth.mail import send_html_email
from Auth.models import Level
from . import models
from .notifications import new_shedule, update_shedule


def superuser_or_staff_required(view_func):
    def check_user(request, *args, **kwargs):
        if not request.user.is_authenticated or (not request.user.is_superuser and not request.user.is_staff):
            return redirect('shedules')
        return view_func(request, *args, **kwargs)

    return check_user


User = get_user_model()


def _update_user(request, admin=None):
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=user_id)

    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone_num = request.POST.get('phone_num')
    level = request.POST.get('classroom')
    is_teacher = bool(request.POST.get('is_teacher'))
    is_staff = bool(request.POST.get('is_staff'))

    avatar = request.FILES.get('avatar')

    if email and first_name and last_name:
        if User.objects.filter(email=email).exclude(id=user_id).exists():
            return "Un utilisateur existe déjà avec cet email"

        if avatar:
            file_extension = avatar.name.split('.')[-1]
            avatar_name = f'{uuid.uuid4().hex}.{file_extension}'

            file_path = f'avatars/{avatar_name}'
            default_storage.save(file_path, avatar)
            user.avatar = file_path

        user.first_name = first_name
        user.last_name = last_name
        user.phone_num = phone_num
        if admin is not None:
            user.email = email
            user.is_teacher = is_teacher
            user.is_staff = is_staff
        else:
            if not user.is_teacher and not user.is_staff and not user.is_superuser:
                level = Level.objects.get(id=level)
                user.level = level
        user.save()

    else:
        return "Veuillez remplir tout les champs"


@login_required
def default(request):

    try:
        total_subject_student = models.Subject.objects.filter(level_id=request.user.level.id).count()
    except:
        total_subject_student = 0

    context = {
        'total_students': User.objects.filter(is_teacher=False, is_superuser=False, is_staff=False).count(),
        'total_teachers': User.objects.filter(is_teacher=True).count(),
        'total_subjects': models.Subject.objects.all().count(),
        'total_classroom': models.Classroom.objects.all().count(),
        'notifications': request.user.notifications.filter(is_opened=False),
        'total_subject_student': total_subject_student,
        'total_subject_w': 2,
        'total_subject_week': 3,
        'total_subject_week_w': 1,
    }

    return render(request, 'app/default.html', context)


@login_required
@superuser_or_staff_required
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
                    errors.append(
                        "Un utilisateur existe déjà avec cet email")

                if avatar and not exist:
                    file_extension = avatar.name.split('.')[-1]
                    avatar_name = f'{uuid.uuid4().hex}.{file_extension}'

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

                try:
                    send_html_email(
                    'Activation de compte WebP2MS',
                    'mails/new-password.html',
                    {'to': user, 'reset_link': reset_link, 'expire': expire_at},
                    [email])

                    User.objects.create(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        is_teacher=is_teacher,
                        is_staff=is_staff,
                        created_by=created_by,
                        avatar=file_path if avatar else None,
                        reset_token=token,
                        reset_token_expiration=timezone.now() + timedelta(hours=expire_at)
                    )
                except:
                    errors.append("Veuillez verifier que vous etes bien connecté afin que le mail contenant les instructions de creation de mot de passe de l'enseignant lui soit transmit, sinon le compte ne pourra pas etre creer")

        elif _method in ['PUT', 'PATCH', 'UPDATE']:
            error = _update_user(request, True)
            if error:
                errors.append(error)

        else:
            errors.append("Veuillez remplir tous les champs obligatoires")

    context = {
        'users': User.objects.filter(Q(is_teacher=True) | Q(is_staff=True)),
        'errors': errors
    }

    return render(request, 'app/teachers.html', context)


@login_required
@superuser_or_staff_required
def students(request):
    levels = Level.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        is_active = bool(request.POST.get('is_active'))

        user = User.objects.get(id=user_id)

        user.is_active = is_active
        user.save()

    context = {
        'users': User.objects.filter(is_teacher=False, is_superuser=False, is_staff=False),
        'levels': levels,
    }

    return render(request, 'app/students.html', context)


@login_required
@superuser_or_staff_required
def cours(request):

    errors, exist = [], False

    if request.method == 'POST':
        slug = request.POST.get('slug')
        code = request.POST.get('code')
        level = request.POST.get('level')
        desc = request.POST.get('desc')
        bgColor = request.POST.get('bgColor')
        total_time = request.POST.get('total_time')
        _method = request.POST.get('method')

        if _method == 'POST':

            if slug and level and total_time:
                if models.Subject.objects.filter(slug=slug, level_id=level).exists():
                    exist = True
                    errors.append("Une matière existe déjà avec cet slug")
            else:
                errors.append("Veuillez remplir tous les champs obligatoires")

            if not exist:
                created_by = User.objects.get(id=request.user.id)
                level = Level.objects.get(id=level)

                models.Subject.objects.create(
                    slug=slug,
                    code=code,
                    level=level,
                    desc=desc,
                    bgColor=bgColor,
                    total_time=total_time,
                    created_by=created_by,
                )

        elif _method in ['PUT', 'PATCH', 'UPDATE']:
            object_id = request.POST.get('object_id')
            subject = models.Subject.objects.get(id=object_id)

            slug = request.POST.get('slug')
            code = request.POST.get('code')
            desc = request.POST.get('desc')
            bgColor = request.POST.get('bgColor')
            level = request.POST.get('level')
            total_time = request.POST.get('total_time')

            if slug and level and total_time:
                level = Level.objects.get(id=level)

                subject.slug = slug
                subject.code = code
                subject.level = level
                subject.desc = desc
                subject.bgColor = bgColor
                subject.total_time = total_time
                subject.save()

        else:
            errors.append("Veuillez remplir tous les champs obligatoires")

    context = {
        'levels': Level.objects.all(),
        'subjects': models.Subject.objects.all(),
        'errors': errors
    }

    return render(request, 'app/courses.html', context)


@login_required
@superuser_or_staff_required
def salles(request):

    errors, exist = [], False

    if request.method == 'POST':
        slug = request.POST.get('slug')
        capacity = request.POST.get('capacity')
        desc = request.POST.get('desc')
        _method = request.POST.get('method')

        if _method == 'POST':

            if slug:
                if models.Classroom.objects.filter(slug=slug).exists():
                    errors.append("Une classe existe déjà avec cet slug")
                else:
                    created_by = User.objects.get(id=request.user.id)

                    models.Classroom.objects.create(
                        slug=slug,
                        capacity=capacity if capacity else 0,
                        desc=desc,
                        created_by=created_by
                    )
            else:
                errors.append("Veuillez remplir tous les champs obligatoires")
            

        elif _method in ['PUT', 'PATCH', 'UPDATE']:
            object_id = request.POST.get('object_id')
            classroom = models.Classroom.objects.get(id=object_id)

            slug = request.POST.get('slug')
            capacity = request.POST.get('capacity')

            if slug and capacity:

                classroom.slug = slug
                classroom.desc = desc
                classroom.capacity = capacity if capacity else 0
                classroom.save()

        else:
            errors.append("Veuillez remplir tous les champs obligatoires")

    context = {
        'classrooms': models.Classroom.objects.all(),
        'errors': errors
    }

    return render(request, 'app/classrooms.html', context)


@login_required
@superuser_or_staff_required
def levels(request):

    errors, exist = [], False

    if request.method == 'POST':
        slug = request.POST.get('slug')
        total_students = request.POST.get('total_students')
        _method = request.POST.get('method')

        if _method == 'POST':

            if slug:
                Level.objects.create(
                    slug=slug,
                    total_students=total_students if total_students else 0
                )
            else:
                errors.append("Veuillez remplir tous les champs obligatoires")
            

        elif _method in ['PUT', 'PATCH', 'UPDATE']:
            object_id = request.POST.get('object_id')
            level = Level.objects.get(id=object_id)

            slug = request.POST.get('slug')
            total_students = request.POST.get('total_students')

            if slug:

                level.slug = slug
                level.total_students = total_students if total_students else 0
                level.save()

        else:
            errors.append("Veuillez remplir tous les champs obligatoires")

    context = {
        'levels': Level.objects.all(),
        'errors': errors
    }

    return render(request, 'app/levels.html', context)


@login_required
def shedules(request):

    context = {
        'subjects': models.Subject.objects.all(),
        'levels': Level.objects.all(),
        'classrooms': models.Classroom.objects.all(),
        'teachers': User.objects.filter(is_teacher=True),
    }

    return render(request, 'app/shedules.html', context)


@login_required
def notifications(request):

    context = {
        'notifications': request.user.notifications.all()
    }

    return render(request, 'app/notifications.html', context)


@login_required
def aides(request):

    context = {}

    return render(request, 'app/helps.html', context)


@login_required
def profile(request):

    context = {
        'levels': Level.objects.all(),
    }

    return render(request, 'app/profile.html', context)


@csrf_exempt
@login_required
@superuser_or_staff_required
def ajax_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        object_id = data.get('object_id')
        model = data.get('model')

        if object_id:
            if model == 'users':
                objects = User
            elif model == 'classrooms':
                objects = models.Classroom
            elif model == 'levels':
                objects = Level
            elif model == 'subjects':
                objects = models.Subject
            elif model == 'notifications':
                object = models.Notification
            elif model == 'chats':
                models.Chat.objects.filter(timetable_id=object_id).delete()
                return JsonResponse({'success': 'Object deleted successfully'})             
            else:
                return False
            try:
                objects = objects.objects.get(id=object_id)
                objects.delete()
                return JsonResponse({'success': 'Object deleted successfully'})
            except User.DoesNotExist:
                return JsonResponse({'error': 'Object not found'}, status=400)
        else:
            return JsonResponse({'error': 'Missing object_id'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)


@csrf_exempt
@login_required
def update_user(request):
    if (request.method == 'POST'):
        action = request.POST.get('action')

        if action == 'DETAILS':
            error = _update_user(request)
            if not error:
                return JsonResponse({'success': 'Votre compte a été mis à jour avec succès'})
            return JsonResponse({'error': error}, status=400)
        elif action == 'EMAIL':

            password = request.POST.get('confirmemailpassword')
            new_email = request.POST.get('emailaddress')

            if password and new_email:
                if request.user.check_password(password):
                    request.user.email = new_email
                    request.user.save()

                    update_session_auth_hash(request, request.user)

                    return JsonResponse({'success': 'Email mis à jour avec succès'})
                else:
                    return JsonResponse({'error': 'Mot de passe incorrect'}, status=400)

        elif action == 'PASSWORD':
            current_password = request.POST.get('currentpassword')
            new_password = request.POST.get('newpassword')
            confirm_password = request.POST.get('confirmpassword')

            if current_password:
                if not check_password(current_password, request.user.password):
                    return JsonResponse({'error': 'Mot de passe actuel incorrect'}, status=400)

            if new_password and confirm_password:
                if new_password != confirm_password:
                    return JsonResponse({'error': 'Les nouveaux mots de passe ne correspondent pas'}, status=400)

                request.user.set_password(new_password)

            request.user.save()
            update_session_auth_hash(request, request.user)
            return JsonResponse({'success': 'Votre mot de passe mis a été jour avec succès'})

    return JsonResponse({'error': 'Invalid HTTP method'}, status=400)


@csrf_exempt
@login_required
def ajax_get_shedules(request):

    if request.user.is_staff or request.user.is_superuser:
        level_id = request.GET.get('level')

        if level_id and level_id != 'default':
            shedules = models.Timetable.objects.filter(
                subject__level_id=level_id)
        else:
            shedules = models.Timetable.objects.all()

    else:
        if request.user.is_teacher:
            shedules = models.Timetable.objects.filter(
            teacher_id=request.user.id)
        else:
            shedules = models.Timetable.objects.filter(
            subject__level_id=request.user.level.id)
    data = [shedule.serialize() for shedule in shedules]

    return JsonResponse(data, safe=False)


@csrf_exempt
@login_required
@superuser_or_staff_required
def ajax_set_shedule(request, pk=None):

    if request.method == 'POST':
        data = request.POST

        teacher = data.get('teacher')
        classroom = data.get('classroom')

        subject = data.get('subject')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if teacher and classroom and subject and start_time and end_time and start_date and end_date:

            try:
                if pk is None:
                    shedule = models.Timetable.objects.create(
                        classroom=models.Classroom.objects.get(id=classroom),
                        subject=models.Subject.objects.get(id=subject),
                        teacher=User.objects.get(id=teacher),
                        start_time=start_time,
                        end_time=end_time,
                        start_date=start_date,
                        end_date=end_date,
                    )
                    new_shedule(shedule)
                else:
                    shedule = models.Timetable.objects.get(id=pk)

                    shedule.classroom = models.Classroom.objects.get(
                        id=classroom)
                    shedule.subject = models.Subject.objects.get(id=subject)
                    shedule.teacher = User.objects.get(id=teacher)
                    shedule.start_time = start_time
                    shedule.end_time = end_time
                    shedule.start_date = start_date
                    shedule.end_date = end_date

                    shedule.save()
                    update_shedule(shedule)
            except:
                return JsonResponse({'error': 'Erreur lors de la création/mise à jour du programme, vérifiez tout vos champs'}, status=400)

            return JsonResponse({'success': "Un nouveau programme ajouté/mise à jour avec sucess", 'shedule': shedule.serialize()})

        else:
            return JsonResponse({'error': 'Veuillez bien remplir tout les champs'}, status=400)

    else:
        return JsonResponse({'error': 'Methode HTTP invalid'}, status=400)


@csrf_exempt
@login_required
@superuser_or_staff_required
def ajax_del_shedule(request):

    data = json.loads(request.body.decode('utf-8'))
    shedule = data.get('shedule_id')

    try:
        shedule = models.Timetable.objects.get(id=shedule)

        shedule.delete()
    except:
        return JsonResponse({'error': 'Erreur lors de la suppression du programme'}, status=400)

    return JsonResponse({'success': "Le programme a été supprimé avec sucess", 'shedule': shedule.serialize()})

@csrf_exempt
@login_required
@superuser_or_staff_required
def ajax_check_shedule(request):
    if request.method == 'POST':
        data = request.POST

        teacher = data.get('teacher')
        classroom = data.get('classroom')

        subject = data.get('subject')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if teacher and classroom and subject and start_time and end_time and start_date and end_date:

            try:
                teacher = User.objects.get(id=teacher)

                models.Timetable.objects.filter()
            except:
                return JsonResponse({'error': 'Veuillez bien selectionner un nom de professeur'}, status=400)
        else:
            return JsonResponse({'error': 'Veuillez bien remplir tout les champs'}, status=400)

    else:
        return JsonResponse({'error': 'Methode HTTP invalid'}, status=400)

@csrf_exempt
@login_required
def get_all_notifications(request):
    notifications = request.user.notifications.filter(is_opened=False)

    data = [n.serialize() for n in notifications]

    return JsonResponse(data, safe=False)


@login_required
def mark_notification(request, pk):
    notifications = request.user.notifications.get(id=pk)

    notifications.is_opened = True
    notifications.save()
    
    return redirect('shedules')
