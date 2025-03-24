from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.service import S3Service
from user.models import Photographer

@receiver(post_save, sender=Photographer)
def create_photographer_folder(sender, instance, created, **kwargs):
    if created:
        s3 = S3Service()
        s3.create_folder(instance.s3_folder)
