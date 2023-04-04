from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image']

class SongSerializer(serializers.ModelSerializer):
    # artist = ArtistSerializer(many=True)
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'album', 'artist']

class AlbumSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'published_date', 'cover_art', 'genre']