from django.db import models


class Organization(models.Model):
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    address = models.CharField(
        max_length=256,
        verbose_name="Адрес",
    )
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    phone_two = models.CharField(
        max_length=15,
        verbose_name="Запасной номер телефона",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
    )
    icon = models.ForeignKey(
        to="gallery.Image",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Иконка",
    )
    social_networks = models.ManyToManyField(
        to="common.SocialMedia",
        verbose_name="Социальные сети",
    )
    coordinates = models.CharField(
        max_length=50,
        verbose_name="Координаты",
        null=True,
        blank=True,
    )
    about_us = models.TextField(
        null=True,
        blank=True,
    )
