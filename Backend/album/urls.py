from django.urls import path, include
from rest_framework import routers

from album.api import (
    AlbumViewSet
)

router = routers.DefaultRouter()

router.register(r'', AlbumViewSet, basename='album-api')

urlpatterns = [
    path('', include(router.urls), name="album")
]

