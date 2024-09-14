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

def game_detail(request, game_id):
    # Fetch the game from your local database using the game_id
    game = get_object_or_404(Game, id=game_id)
    
    # Fetch game details from the RAWG API using the stored `rawg_id`
    game_data = fetch_game_details(game.rawg_id)

    if game_data:
        context = {
            'title': game_data.get('name', 'Unknown'),
            'image_link': game_data.get('background_image', ''),
            'description': game_data.get('description', 'No description available'),
            'rating': game_data.get('rating', 'N/A'),
            'release_date': game_data.get('released', 'Unknown'),
            'publisher': ', '.join([publisher['name'] for publisher in game_data.get('publishers', [])]) or 'Unknown',
            'developer': ', '.join([developer['name'] for developer in game_data.get('developers', [])]) or 'Unknown',
        }
    else:
        context = {'error': 'Game details not found'}

    return render(request, 'GS/game_detail.html', context)



