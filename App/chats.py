from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Timetable


def chats(request):
    
    context = {

    }

    return render(request, 'app/chats.html', context)