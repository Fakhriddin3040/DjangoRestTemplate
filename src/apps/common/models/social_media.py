from django.db import models


class SocialMedia(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ("youtube", "youtube"),
        ("twitter", "twitter"),
        ("instagram", "instagram"),
        ("linkedin", "linkedin"),
        ("fb", "facebook"),
        ("telegram", "telegram"),
        ("whatsapp", "whatsApp"),
    ]

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    link = models.CharField(
        max_length=1024,
        verbose_name="Ссылка",
    )
    social_type = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES)
