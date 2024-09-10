from django.shortcuts import render
from .utils import fetch_games

def home(request):
    games = fetch_games()
    # Ensure genres are just names
    for game in games:
        if 'genres' in game:
            game['genres'] = [genre['name'] for genre in game.get('genres', [])]
        else:
            game['genres'] = []  # Ensure 'genres' is always a list
    return render(request, 'GS/home.html', {'games': games})
