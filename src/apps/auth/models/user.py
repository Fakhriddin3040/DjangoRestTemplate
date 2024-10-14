from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.images import ImageFile
from src.apps.auth.managers.user_manager import UserManager


class User(AbstractUser):
    objects = UserManager()

    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты")
    username = models.CharField(
        max_length=150, unique=True, verbose_name="Имя пользователя"
    )
    password = models.CharField(max_length=128, null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Номер телефона"
    )
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user: User = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    bio: str = models.TextField(max_length=500, blank=True, verbose_name="О себе")
    avatar: ImageFile = models.ImageField(
        upload_to="avatars/", null=True, blank=True, verbose_name="Аватар"
    )
    address: str = models.CharField(max_length=255, blank=True, verbose_name="Адрес")
    postal_code: str = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="Почтовый индекс"
    )

    def __str__(self):
        return self.user.email


class UserTempData(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="oauth2_data", null=True
    )

    otp = models.CharField(max_length=40, blank=True, null=True)

    expired_time = models.DateTimeField(verbose_name="Время истечения")

    target_value = models.CharField(max_length=255)

    verified = models.BooleanField(
        default=False,
    )


class OAuth2(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Пользователь", null=True
    )

    token = models.CharField(verbose_name="Токен", max_length=255)
