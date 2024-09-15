# views.py
import requests
from django.shortcuts import render, get_object_or_404
from .models import Game
from .utils import fetch_game_details

def home(request):
    return render(request, 'GS/home.html')

def catalog(request):
    games = Game.objects.all()  # Fetch all games from the database
    return render(request, 'GS/catalog.html', {'games': games})

from django.shortcuts import render, get_object_or_404
from .models import Game
from .utils import fetch_game_details

def game_detail(request, game_id):
    # Fetch the game from your local database using the game_id
    game = get_object_or_404(Game, id=game_id)
    
    # Fetch game details from the RAWG API using the stored `rawg_id`
    game_data = fetch_game_details(game.rawg_id)

    if game_data:
        context = {
            'title': game_data.get('title', 'Unknown'),
            'image_link': game_data.get('background_image', ''),
            'description': game_data.get('description', 'No description available'),
            'rating': game_data.get('rating', 'N/A'),
            'release_date': game_data.get('release_date', 'Unknown'),
            'publisher': game_data.get('publisher', 'Unknown'),
            'developer': game_data.get('developer', 'Unknown'),
        }
    else:
        context = {'error': 'Game details not found'}

    return render(request, 'GS/game_detail.html', context)




