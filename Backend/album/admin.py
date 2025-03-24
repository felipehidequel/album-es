from django.contrib import admin

from album.models import Album


class AlbumAdmin(admin.ModelAdmin):
    model = Album

    list_display = ('id', 'name_album', 'photographer', 'created_at_album')

    search_fields = ('name_album',)
    ordering = ('id',)

admin.site.register(Album, AlbumAdmin)
