from .models import Notification
from django.db.models import Q
from Auth.models import MyUser as User
from Auth.mail import send_html_email


def new_shedule(shedule):
    student_message = f"Un nouveau emploi du temps programmé pour le {shedule.start_date}"
    teacher_message = f"Vous êtes programmé pour le {shedule.start_date} en {shedule.subject.level.slug}"
    message = ''
    levelId = shedule.subject.level.id
    users = User.objects.filter(Q(id=shedule.teacher_id) | Q(level=levelId))

    for user in users:
        if user.is_teacher:
            message = teacher_message
        else:
            message = student_message

        Notification.objects.create(
            user=user,
            message=message,
            category='shedule',
            elt=shedule.id,
        )

        try:
            send_html_email("Nouveau Emploi du Temps", 'mails/new-shedule.html', {
                'message': message,
                'to': user
            })
        except:
            continue


def update_shedule(shedule):
    student_message = f"un emploi du temps pour le {shedule.start_date} a été mis à jour"
    teacher_message = f"Votre programme pour le {shedule.start_date} en {shedule.objects.level.slug} a été mis à jour"
    message = ''
    levelId = shedule.subject.level.id
    users = User.objects.filter(Q(id=shedule.teacher_id) | Q(level=levelId))

    for user in users:
        if user.is_teacher:
            message = teacher_message
        else:
            message = student_message

        Notification.objects.create(
            user=user,
            message=message,
            category='shedule',
            elt=shedule.id,
        )
        try:
            send_html_email("Mise à jour d'un Emploi du Temps", 'mails/update-shedule.html', {
                'message': message,
                'to': user
            })
        except:
            continue


def new_chat(request, chat):

    message = f"Vous avez réçu un nouveau message"

    if request.user.is_superuser or request.user.is_staff:
        teacher = User.objects.get(id=chat.timetable.teacher.id)

        Notification.objects.create(
            user=teacher,
            message=message,
            category='chat',
            elt=chat.timetable.id,
        )

        if not teacher.is_online:
            try:
                send_html_email("Nouveau Message sur votre Emploi du temps", 'mails/new-chat.html', {
                    'message': message,
                    'to': teacher
                })
            except:
                return False

    elif request.user.is_teacher:
        users = User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))

        for user in users:
            Notification.objects.create(
                user=user,
                message=message,
                category='chat',
                elt=chat.timetable.id,
            )
