import uuid
from django.db import models
from django.contrib.auth.models import User

from gallery.utils import generate_custom_id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Photographer(Profile):
    name_photographer = models.CharField(max_length=60)
    name_company = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    s3_folder = models.CharField(max_length=255, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.s3_folder:
            self.s3_folder = f"{generate_custom_id(f"{self.name_photographer}")}/"
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_user} - {self.name_photographer}"

    class Meta:
        verbose_name = "Photographer"
        verbose_name_plural = "Photographers"
