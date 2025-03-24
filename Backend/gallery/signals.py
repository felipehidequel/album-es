import os
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from backend.service import S3Service
from gallery.utils import generate_custom_id
from .models import Album, Photo

@receiver(post_save, sender=Album)
def create_album_folder(sender, instance, created, **kwargs):
    if created:
        s3 = S3Service()
        s3.create_folder(instance.s3_path_album)

@receiver(pre_save, sender=Photo)
def set_photo_path(sender, instance, **kwargs):
    if instance.photo and not instance.s3_path_photo and instance.album.s3_path_album:
        ext = os.path.splitext(instance.photo.name)[1]
        unique_filename = f"{generate_custom_id(ext)}"

        instance.s3_path_photo = f"{instance.album.s3_path_album}{unique_filename}"
        instance.photo.name = instance.s3_path_photo
