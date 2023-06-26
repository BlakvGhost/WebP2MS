from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Timetable


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

    context = {
        'shedules': correct_shedule(request),
    }

    return render(request, 'app/chats.html', context)

@login_required
@superuser_or_staff_or_teacher_required
def chat(request, spk):

    context = {
        'shedules': correct_shedule(request),
    }

    return render(request, 'app/chats-details.html', context)