# Generated by Django 5.1.7 on 2025-03-24 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_created_at_album_alter_album_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at_album',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 24, 9, 29, 52, 306631), verbose_name='Album creation date'),
        ),
    ]
