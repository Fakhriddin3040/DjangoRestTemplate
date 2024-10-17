from django.db import models


class SocialMedia(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ("youtube", "Youtube"),
        ("twitter", "Twitter"),
        ("instagram", "Instagram"),
        ("linkedin", "LinkedIn"),
        ("fb", "Facebook"),
        ("telegram", "Telegram"),
        ("whatsapp", "WhatsApp"),
    ]

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    link = models.CharField(
        max_length=1024,
        verbose_name="Ссылка",
    )
    icon = models.ImageField(verbose_name="Иконка")
    social_type = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES)
