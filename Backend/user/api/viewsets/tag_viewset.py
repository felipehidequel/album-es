from rest_framework import viewsets, permissions

from user.models import Tag
from ..serializers.tag_serializar import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
