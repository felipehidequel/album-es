from django.apps import AppConfig


class AlbumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'

    def ready(self):
        import gallery.signals
