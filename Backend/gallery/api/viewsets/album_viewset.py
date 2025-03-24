from rest_framework import viewsets, permissions
from gallery.models import Album
from ..serializers.album_serializer import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [permissions.IsAuthenticated]
