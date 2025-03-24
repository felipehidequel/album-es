from django.contrib import admin

from gallery.models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    model = Album

    list_display = ('id', 'name_album', 'photographer', 'created_at_album')

    search_fields = ('name_album',)
    ordering = ('id',)

admin.site.register(Album, AlbumAdmin)

class PhotoAdmin(admin.ModelAdmin):
    model = Photo

    list_display = ('id', 'name_photo')

    search_fields = ('name_album',)
    ordering = ('id',)

admin.site.register(Photo, PhotoAdmin)
