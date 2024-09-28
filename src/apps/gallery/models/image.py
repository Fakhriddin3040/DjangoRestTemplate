from django.db import models

from src.base.mixins import models as model_mixins
from src.apps.gallery.managers.image import ImageManager


def upload_to(instance, filename) -> str:
    return "images/{}".format(filename)


class Image(
    models.Model,
    model_mixins.AbstractAuditModelsFields,
    model_mixins.AbstractTimestambleModelFields,
):
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    objects = ImageManager()

    title = models.CharField(
        verbose_name="Название",
        max_length=100,
        blank=True,
    )
    image = models.ImageField(
        upload_to=upload_to,
        verbose_name="Оригинальное изображение",
    )
    url = models.URLField(
        verbose_name="Ссылка на изображение",
        unique=True,
        blank=True,
        null=True,
    )
