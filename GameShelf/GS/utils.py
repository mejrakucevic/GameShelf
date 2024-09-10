import requests

def fetch_games():
  url = "https://rawg-video-games-database.p.rapidapi.com/games"
  headers = {
	"x-rapidapi-key": "cb5fadfba7msh807f17f55e2e914p1cf5d9jsne86a10a34850",
	"x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com"
}
  params = {
    "key": "8cf3a81e6fe7452b9228249eafd7d334",
    "page_size": 30
}

  try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('results', [])
  except requests.exceptions.RequestException as e:
        print(f"Error fetching data from RAWG API: {e}")
        return []

