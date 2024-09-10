# views.py

from django.shortcuts import render
from .models import Game


def home(request):
    games = Game.objects.all()  # Ensure this line returns a queryset
    # Check if games is None
    if games is None:
        games = []  # Handle None by assigning an empty list
    return render(request, 'GS/home.html', {'games': games})

