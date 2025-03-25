from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import os
from uuid import uuid4
from django.core.files.storage import default_storage
from django.utils.text import slugify

from .album import Album
from gallery.utils import generate_custom_id

class PhotoStorage(S3Boto3Storage):
    file_overwrite = False
    default_acl = 'private'
    
    def get_valid_name(self, name):
        name = name.replace('\\', '/')
        name = os.path.normpath(name).replace('\\', '/')

        return super().get_valid_name(name)
    
    def generate_filename(self, filename):
        filename = filename.replace('\\', '/')
        filename = os.path.normpath(filename).replace('\\', '/')

        return super().generate_filename(filename)

class Photo(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE,
        verbose_name="Photo album"
    )

    name_photo = models.CharField(
        max_length=60,
        verbose_name="Photo name"
    )

    photo = models.FileField(
        storage=PhotoStorage(),
        upload_to='',
        max_length=500,
        verbose_name="Photo file"
    )
    
    s3_path_photo = models.CharField(
        max_length=500,
        blank=True, 
        editable=False,
        verbose_name="Photo path S3"
    )

    @property
    def format_photo(self):
        return os.path.splitext(self.photo.name)[1][1:].upper() if self.photo else ''

    @property
    def size_photo(self):
        return self.photo.size if self.photo else 0

    def clean_path(self, path):
        path = os.path.normpath(path).replace('\\', '/')

        return path.replace('//', '/')

    def save(self, *args, **kwargs):
        if not self.s3_path_photo and hasattr(self, 'album') and self.album.s3_path_album:
            clean_album_path = self.clean_path(self.album.s3_path_album)
            
            if not clean_album_path.endswith('/'):
                clean_album_path += '/'
            
            ext = os.path.splitext(self.photo.name)[1] if self.photo else '.jpg'
            unique_filename = f"{generate_custom_id(self.name_photo)}{ext}"
            
            self.s3_path_photo = self.clean_path(f"{clean_album_path}{unique_filename}")
            
            if self.photo:
                self.photo.name = self.s3_path_photo
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name_photo}"

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['id', 'name_photo']
