from django.db import models

from user.models import Photographer, Tag
from gallery.utils import generate_custom_id


class Album(models.Model):
    name_album = models.CharField(
        max_length=50,
        verbose_name="Album name"
    )

    photographer = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        verbose_name="Photographer"
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name="Album tag list",
        null=True,
        blank=True
    )

    s3_path_album = models.CharField(
        max_length=255, 
        blank=True, 
        editable=False,
        verbose_name="Album path S3"
    )

    created_at_album = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Album creation date"
    )

    updated_at_album = models.DateTimeField(
        auto_now=True,
        verbose_name="Album update date"
    )

    def __str__(self):
        return f"{self.id} - {self.name_album}"
    
    def save(self, *args, **kwargs):
        if not self.s3_path_album:
            self.s3_path_album = f"{self.photographer.s3_folder}albums/{generate_custom_id(self.name_album)}/"
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Album",
        verbose_name_plural = "Albuns"
        ordering = ['id', 'name_album']
