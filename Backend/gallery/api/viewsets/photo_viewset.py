from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from gallery.models import Photo
from ..serializers.photo_serializer import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            photo = serializer.save()
            return Response({
                'id': photo.id,
                'album': photo.album_id,
                'name_photo': photo.name_photo,
                'photo_path': photo.photo.name,
                'format_photo': photo.format_photo,
                'size_photo': photo.size_photo
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'error': str(e),
                'details': 'Falha ao processar o upload da foto'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)