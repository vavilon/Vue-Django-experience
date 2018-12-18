from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户资料
    """
    email = models.EmailField(verbose_name="pochtovyy yashchik")
    point = models.PositiveIntegerField(default=0, verbose_name="integratsiya")

    class Meta:
        verbose_name = "Profil' pol'zovatelya"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def increase_point(self):
        self.point += 1
        self.save(update_fields=['point'])
