from django.db import models

from src.base.mixins import models as model_mixins
from src.apps.gallery.managers.slide import SlideManager


class Slide(
    models.Model,
    model_mixins.AbstractTimestambleModelFields,
    model_mixins.AbstractAuditModelsFields,
):
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ("turn",)

    objects = SlideManager()
    title = models.CharField(
        verbose_name="Название",
        max_length=100,
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=300,
        blank=True,
        null=True,
    )
    turn = models.SmallIntegerField(
        verbose_name="Очередь",
        null=True,
        blank=True,
    )
    image = models.ForeignKey(
        to="gallery.Image",
        on_delete=models.CASCADE,
        verbose_name="Изображение",
    )
    link = models.URLField(
        verbose_name="Ссылка",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name="Статус активности",
        default=True,
    )

    def deactivate(self) -> None:
        self.is_active = False
        self.turn = None
        self.save()
