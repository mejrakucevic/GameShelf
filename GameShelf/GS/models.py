from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    developer = models.CharField(max_length=255, blank=True, null=True)
    publishers = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    rawg_id = models.IntegerField()  # Store the RAWG API game ID

    
