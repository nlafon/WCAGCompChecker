from django.shortcuts import render

from .models import checkRequest


def requestView(request):

    context = {}
    
    return render(request, 'home.html', context)
