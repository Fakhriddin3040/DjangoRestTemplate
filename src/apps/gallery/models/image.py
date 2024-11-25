from django.db import models
from ..managers import image as image_manager
from ..const import PRODUCT_IMAGES_PATH


class Image(models.Model):
    objects = image_manager.ImageManager()

    ext_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Оригинал", upload_to=PRODUCT_IMAGES_PATH, blank=True, null=True
    )
    url = models.URLField(
        max_length=550,
        null=True,
        blank=True,
    )
