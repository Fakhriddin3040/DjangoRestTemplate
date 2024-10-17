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
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", null=True, blank=True)
    phone_two = models.CharField(
        max_length=15,
        verbose_name="Запасной номер телефона",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        null=True,
        blank=True,
    )
    icon = models.ImageField(verbose_name="Иконка", null=True, blank=True,)
    social_media = models.CharField(verbose_name="Социальные сети", max_length=25, null=True, blank=True)
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
