from django.apps import AppConfig


class BarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bar'

    verbose_name = 'Бар'
    verbose_name_plural = 'Бар'
