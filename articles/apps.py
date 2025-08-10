from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    label = 'custom_articles'  # لمنع التضارب
