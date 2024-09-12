# views.py

from django.shortcuts import render
from .models import Game


def home(request):
    return render(request, 'GS/home.html')
    
def catalog(request):
    games = Game.objects.all()
    return render(request, 'GS/catalog.html', {'games': games})

    

