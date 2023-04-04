from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=500)

class Playlist(models.Model):
    name = models.CharField(max_length=500)

class Artist(models.Model):
    name = models.CharField(max_length=500)
    bio = models.TextField()
    image = models.URLField(max_length=200, null=True)
