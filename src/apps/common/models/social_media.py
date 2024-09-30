from django.db import models


class SocialMedia(models.Model):
    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    title = models.CharField(
        max_length=100,
        verbose_name="Наввание",
    )
    link = models.CharField(
        max_length=1024,
        verbose_name="Ссылка",
    )
    icon = models.ForeignKey(
        to="gallery.Image",
        on_delete=models.SET_NULL,
        verbose_name="Иконка",
        null=True,
        blank=True,
    )
