from django.db import models

from ..managers import ProductManager


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    objects = ProductManager()

    identifier = models.CharField(
        max_length=100,
        verbose_name="Идентификатор",
    )
