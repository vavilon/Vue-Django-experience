from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'Blog'
    verbose_name = "文章管理"
    verbose_name_plural = verbose_name
