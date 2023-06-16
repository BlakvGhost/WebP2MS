from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def default(request):
    
    context = {}
    
    return render(request, 'app/default.html', context)

@login_required
def teachers(request):
    
    context = {}
    
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