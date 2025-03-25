from django.db import models

from user.models import Photographer


class Tag(models.Model):
    name_tag = models.CharField(
        max_length=20,
        verbose_name="Tag name"
    )

    photographer = models.ForeignKey(
        Photographer, 
        on_delete=models.CASCADE, 
        verbose_name="Photographer"
    )

    def __str__(self):
        return f"{self.id} - {self.name_tag}"
    
    class Meta:
        verbose_name = "Tag",
        verbose_name_plural = "Tags"
        ordering = ['id', 'name_tag']
