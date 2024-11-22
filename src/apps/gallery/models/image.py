from django.db import models
from ..managers import image as image_manager


class Image(models.Model):
    objects = image_manager.ImageManager()

    original = models.ImageField(
        verbose_name="Оригинал",
    )
    url = models.URLField(
        max_length=550,
    )
