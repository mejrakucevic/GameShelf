# views.py

from django.shortcuts import render
from .models import Game


def home(request):
    return render(request, 'GS/home.html')
    



