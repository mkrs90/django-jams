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

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image']

class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'published_date', 'cover_art', 'genre']

class AlbumReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'published_date', 'cover_art', 'genre']        

class SongWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'album', 'artist']

class SongReadSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True, read_only=True)
    album = AlbumReadSerializer()
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'album', 'artist']        


class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'song']

class PlaylistReadSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']

    def get_songs(self, obj):
        song = Song.objects.all()
        return [{"id": song.id, "name": song.name} for song in song]


