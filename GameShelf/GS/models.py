from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, blank=True)
    developer = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    platform = models.CharField(max_length=200, blank=True)  # Add this field
    release_date = models.DateField(null=True, blank=True)
    image_link = models.URLField(blank=True)
    exclusive = models.BooleanField(default=False)
    description = models.TextField(blank=True)  # Ensure this field exists
    rating = models.IntegerField(default=0)
