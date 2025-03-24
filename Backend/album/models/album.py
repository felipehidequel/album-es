import uuid
from django.db import models
from datetime import datetime

from user.models import Photographer, Tag


class Album(models.Model):
    uuid_album = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name="Album UUID"
    );

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
        verbose_name="Album tag list"
    )

    link_album = models.URLField(
        verbose_name="Album link"
    )

    created_at_album = models.DateTimeField(
        default=datetime.now(),
        verbose_name="Album creation date"
    )

    updated_at_album = models.DateTimeField(
        auto_now=True,
        verbose_name="Album update date"
    )

    def __str__(self):
        return f"{self.id} - {self.name_album}"
    
    class Meta:
        verbose_name = "Album",
        verbose_name_plural = "Albuns"
        ordering = ['id', 'name_album']
