from django.apps import AppConfig


class XssAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xss_app'
