from django.urls import path, include
from rest_framework import routers

from user.api import (
    PhotographerViewSet,
    LoginAPI,
    TagViewSet
)

router = routers.DefaultRouter()

router.register(r'', PhotographerViewSet, basename='photographer-api')
router.register(r'tag', TagViewSet, basename='tag-api')

urlpatterns = [
    path('', include(router.urls), name="user"),
    path('login', LoginAPI.as_view(), name="login")
]
