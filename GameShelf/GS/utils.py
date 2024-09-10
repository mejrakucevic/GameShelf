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
    "page_size": 35
}
  
  response = requests.get(url, headers=headers, params=params)
  data = response.json()

  for game in data.get('results', []):
        rating_string = game.get('rating', '0')  # Default to '0' if not available

    # Convert the rating to an integer, handle potential conversion errors
        try:
          rating = int(float(rating_string))  # Convert to float first if it's a decimal number
        except (ValueError, TypeError):
          rating = 0  # Fallback value for invalid data
        print(f"Rating: {rating}, Description: {description}")  # Debug output

        Game.objects.update_or_create(
            title=game.get('name'),
            defaults={
                'genre': ', '.join([genre['name'] for genre in game.get('genres', [])]),
                'developer': ', '.join([developer['name'] for developer in game.get('developers', [])]),
                'publisher': ', '.join([publisher['name'] for publisher in game.get('publishers', [])]),
                'platform': ', '.join([platform['platform']['name'] for platform in game.get('platforms', [])]),  # Extracting platforms
                'release_date': game.get('released'),
                'image_link': game.get('background_image', ''),
                'exclusive': False,
                'description': game.get('description', ''),  # Adjust as needed
                'rating': game.get('rating'),
            }
        )