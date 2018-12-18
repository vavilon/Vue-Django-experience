from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """
    Blog Category
    """
    text = models.CharField(max_length=200, verbose_name="kategoriya",)

    class Meta:
        verbose_name = 'vid'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text


class Article(models.Model):
    """
    Blog Article
    """
    title = models.CharField(max_length=250, verbose_name="zagolovok")
    body = models.TextField(verbose_name="tekst")
    author = models.ForeignKey(User, related_name="article", verbose_name="avtor"
                                , on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data sozdaniya")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data obnovleniya")
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name="article", blank=True,
                    null=True, verbose_name="vid", on_delete=models.CASCADE,)

    class Meta:
        ordering = ('-updated',)
        verbose_name = "stat'ya"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    """
    Blog Comment
    """
    article = models.ForeignKey(Article, related_name="comment", verbose_name="stat'ya"
                                , on_delete=models.CASCADE,)
    content = models.CharField(max_length=250, verbose_name="soderzhaniye")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data sozdaniya")
    author = models.ForeignKey(User, related_name="comment", verbose_name="avtor"
                                , on_delete=models.CASCADE,)

    class Meta:
        ordering = ('-created',)
        verbose_name = "obzor"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
