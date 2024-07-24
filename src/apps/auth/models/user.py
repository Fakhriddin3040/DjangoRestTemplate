from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.images import ImageFile


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    bio: str = models.TextField(max_length=500, blank=True)
    avatar: ImageFile = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return self.user.email
