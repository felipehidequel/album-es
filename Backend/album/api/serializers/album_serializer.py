from rest_framework import serializers

from album.models import Album
from user.api import TagSerializer


class AlbumSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            'uuid_album', 'name_album', 'photographer', 'tags', 
            'link_album', 'created_at_album', 'updated_at_album'
        ]
        read_only_fields = ['uuid_album', 'created_at_album', 'updated_at_album']