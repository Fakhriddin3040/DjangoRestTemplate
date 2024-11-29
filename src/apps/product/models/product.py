from django.db import models

from ..managers import ProductManager


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    objects = ProductManager()

    ext_id = models.CharField(
        max_length=50,
        verbose_name="ID во внешнем сервисе",
        unique=True,
    )
    ext_cat_id = models.CharField(
        max_length=50,
        verbose_name="ID категории во внешнем сервисе",
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        null=True,
        blank=True,
    )
    images = models.ManyToManyField(
        to="gallery.Image",
        verbose_name="Изображения",
        related_name="product_images",
    )
    category = models.ForeignKey(
        "category.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        null=True,
    )
    on_sale = models.BooleanField(
        default=False,
        verbose_name="В продаже",
    )
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Скидка", null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )
    count = models.PositiveIntegerField(
        verbose_name="Количество",
        default=0,
    )
    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Вес",
        null=True,
        blank=True,
    )
    brand = models.CharField(
        max_length=255,
        verbose_name="Бренд",
        null=True,
        blank=True,
    )
    model = models.JSONField(
        verbose_name="Модели",
        null=True,
        blank=True,
        encoder=None,
        decoder=None,
    )
    colors = models.JSONField(
        verbose_name="Цвета",
        null=True,
        blank=True,
    )
    vendor_code = models.CharField(
        max_length=255,
        verbose_name="Артикул",
        null=True,
        blank=True,
    )
    production_year = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        null=True,
        blank=True,
    )
