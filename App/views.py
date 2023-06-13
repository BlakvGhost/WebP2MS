from django.shortcuts import render


def default(request):
    
    context = {}
    
    return render(request, 'app/default.html', context)