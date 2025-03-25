from django.contrib import admin

from user.models import Photographer, Tag


class PhotographerAdmin(admin.ModelAdmin):
    model = Photographer

    list_display = ('id', 'name_photographer', 'name_company', 'phone')

    search_fields = ('name_photographer', 'name_company')
    ordering = ('name_photographer',)

admin.site.register(Photographer, PhotographerAdmin)

class TagAdmin(admin.ModelAdmin):
    model = Tag

    list_display = ('id', 'name_tag', 'photographer')

    search_fields = ('name_tag',)
    ordering = ('id', 'name_tag')

admin.site.register(Tag, TagAdmin)