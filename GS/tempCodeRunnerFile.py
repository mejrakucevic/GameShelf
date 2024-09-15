  for game in data.get('results', []):
        print(game.get('publishers', []))
        print(game.get('rating'))
        print(game.get('description', ''))
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