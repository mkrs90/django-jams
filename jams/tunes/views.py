from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

# Create your views here.

def view_genre(request, genre_id):
    print(genre_id)
    selected_genre = Genre.objects.get(pk = genre_id)
    print(selected_genre)
    return HttpResponse('<h1>Name: %s </h1>' % selected_genre.name)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            print("you did either a PUT, PATCH, POST, or DESTROY")
            return PlaylistWriteSerializer
        print("You did a GET")
        return PlaylistReadSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            print("you did either a PUT, PATCH, POST, or DESTROY")
            return AlbumWriteSerializer
        print("You did a GET")
        return AlbumReadSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            print("you did either a PUT, PATCH, POST, or DESTROY")
            return SongWriteSerializer
        print("You did a GET")
        return SongReadSerializer