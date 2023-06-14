from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def default(request):
    
    context = {}
    
    return render(request, 'app/default.html', context)