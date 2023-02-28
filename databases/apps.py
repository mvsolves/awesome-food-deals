from django.apps import AppConfig


class DatabasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'databases'

    def ready(self):
        import databases.signals
