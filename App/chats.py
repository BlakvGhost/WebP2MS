from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Timetable, Chat
from Auth.models import MyUser as User, Level


def superuser_or_staff_or_teacher_required(view_func):
    def check_user(request, *args, **kwargs):
        if not request.user.is_authenticated or (not request.user.is_superuser and not request.user.is_staff and not request.user.is_teacher):
            return redirect('shedules')
        return view_func(request, *args, **kwargs)

    return check_user

def correct_shedule(request):
    if request.user.is_teacher:
        shedules = Timetable.objects.filter(teacher_id=request.user.id)
    else:
        shedules = Timetable.objects.all()
    return shedules


@login_required
@superuser_or_staff_or_teacher_required
def chats(request):    
    shedules = correct_shedule(request)
    chats = [shedule.chats.last() for shedule in shedules]

    context = {
        'shedules': shedules,
        'chats': chats,
        'levels': Level.objects.all(),
    }

    return render(request, 'app/chats.html', context)

@login_required
@superuser_or_staff_or_teacher_required
def chat(request, spk):

    try:
        shedule = Timetable.objects.get(id=spk)
        chats = shedule.chats.last()
    except Timetable.DoesNotExist:
        return redirect('chats')

    context = {
        'shedules': correct_shedule(request),
        'chat': chats,
    }

    return render(request, 'app/chats-details.html', context)

@csrf_exempt
@login_required
@superuser_or_staff_or_teacher_required
def get_all_chats(request):
    shedule = request.GET['shedule_id']
    shedule = Timetable.objects.get(id=shedule)
    chats = shedule.chats.all()
    chats = [chat.serialize() for chat in chats]
    return JsonResponse(chats, safe=False)

@login_required
@superuser_or_staff_or_teacher_required
def begin_chat(request):
    shedule = request.POST.get('shedule_id')

    if shedule:

        shedule = Timetable.objects.get(id=shedule)

        if shedule.chats.all().count() < 1:

            if request.user.is_teacher:
                message = "Bonjour Administration,"
            else:
                message = "Bonjour Professeur,"

            Chat.objects.create(
                timetable=shedule,
                message=message
            )

        return redirect('chats.details', shedule.id)
    return redirect('chats')