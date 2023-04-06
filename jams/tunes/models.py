from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=500)
    bio = models.TextField()
    image = models.URLField(max_length=200, null=True)

class Song(models.Model):
    name = models.CharField(max_length=500)
    duration = models.FloatField()
    album = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)
    artist = models.ManyToManyField(Artist, help_text='Select an artist for this song')

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=500)
    song = models.ManyToManyField(Song, help_text='Select an song for this playlist')

class Album(models.Model):
    name = models.CharField(max_length=500)
    published_date = models.DateField()
    cover_art = models.URLField(max_length=200, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this album')
