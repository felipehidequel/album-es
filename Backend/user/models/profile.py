from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.type_user}"


class Photographer(Profile):
    name_photographer = models.CharField(max_length=60)
    name_company = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Photographer"
        verbose_name_plural = "Photographers"

