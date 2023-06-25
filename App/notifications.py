from .models import Timetable, Notification
from Auth.models import MyUser as User
from Auth.mail import send_html_email

def new_shedule(shedule):
    student_message = f"Un nouveau emploi du temps programmé pour le {shedule.start_date}"
    teacher_message = f"Vous êtes programmé pour le {shedule.start_date} en {shedule.level.slug}"
    message = ''
    users = User.objects.all()

    for user in users:
        if user.is_teacher:
            message = teacher_message
        elif not user.is_staff and not user.is_superuser and user.is_teacher:
            message = student_message
        Notification.objects.create(
            user=user,
            message=teacher_message
        )
        try:
            send_html_email("Nouveau Emploi du Temps", 'mails/new-shedule.html', {
                'message': message,
                'to': user
            })
        except:
            pass



def update_shedule(shedule):
    student_message = f"un emploi du temps pour le {shedule.start_date} a été mis à jour"
    teacher_message = f"Votre programme pour le {shedule.start_date} en {shedule.level.slug} a été mis à jour"
    message = ''
    users = User.objects.all()

    for user in users:
        if user.is_teacher:
            message = teacher_message
        elif not user.is_staff and not user.is_superuser and user.is_teacher:
            message = student_message
        Notification.objects.create(
            user=user,
            message=teacher_message
        )
        try:
            send_html_email("Mise à jour d'un Emploi du Temps", 'mails/update-shedule.html', {
                'message': message,
                'to': user
            })
        except:
            pass
