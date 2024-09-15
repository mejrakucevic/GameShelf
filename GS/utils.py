import requests
from .models import Game

def fetch_games():
  url = "https://rawg-video-games-database.p.rapidapi.com/games"
  headers = {
	"x-rapidapi-key": "cb5fadfba7msh807f17f55e2e914p1cf5d9jsne86a10a34850",
	"x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com"
}
  params = {
    "key": "8cf3a81e6fe7452b9228249eafd7d334",
    "page_size": 20
}
  
  response = requests.get(url, headers=headers, params=params)
  data = response.json()

  for game in data.get('results', []):
        # Debug prints to verify data
        print(f"Publishers: {game.get('publishers', [])}")
        print(f"Rating: {game.get('rating')}")
        print(f"Description: {game.get('description', '')}")

        # Handle rating, default to 0 if not available or if there's an error
        rating_string = game.get('rating', '0')
        try:
            rating = int(float(rating_string))  # Convert to float first, then to integer
        except (ValueError, TypeError):
            rating = 0  # Default rating if there's an error

        # Ensure description exists and handle cases where it's not present
        description = game.get('description', 'No description available')

        # Update or create the game object
        Game.objects.update_or_create(
            title=game.get('name'),
           defaults={
        'rawg_id': game.get('id'),  # Save RAWG API's unique game ID
        'genre': ', '.join([genre['name'] for genre in game.get('genres', [])]),
        'developer': ', '.join([developer['name'] for developer in game.get('developers', [])]) or 'Unknown',
        'publishers': ', '.join([publishers['name'] for publishers in game.get('publishers', [])]) or 'Unknown',
        'platform': ', '.join([platform['platform']['name'] for platform in game.get('platforms', [])]),
        'release_date': game.get('released'),
        'image_link': game.get('background_image', ''),
        'description': game.get('description', 'No description available'),
        'rating': game.get('rating', 0),
            }
        )
        
        
        
def fetch_game_details(game_id):
    url = f"https://api.rawg.io/api/games/{game_id}"
    headers = {
	"x-rapidapi-key": "cb5fadfba7msh807f17f55e2e914p1cf5d9jsne86a10a34850",
	"x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com"
}
    params = {
        "key": "8cf3a81e6fe7452b9228249eafd7d334"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        game_data = response.json()
        
        # Mapping fields correctly based on API response
        game_details = {
            'title': game_data.get('name', 'Unknown'),
            'description': game_data.get('description', 'No description available'),
            'rating': game_data.get('rating', 'N/A'),
            'release_date': game_data.get('released', 'Unknown'),
            'background_image': game_data.get('background_image', ''),
            'publisher': ', '.join(publisher['name'] for publisher in game_data.get('publishers', [])) if 'publishers' in game_data else 'Unknown',
            'developer': ', '.join(developer['name'] for developer in game_data.get('developers', [])) if 'developers' in game_data else 'Unknown',
            'website': game_data.get('website', 'N/A'),
        }
        
        return game_details
    else:
        return None