from rest_framework import serializers

from gallery.models import Album
from user.api import TagSerializer


class AlbumSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['name_album', 'photographer', 'tags', 'created_at_album', 'updated_at_album']
        read_only_fields = ['s3_path_album', 'created_at_album', 'updated_at_album']
