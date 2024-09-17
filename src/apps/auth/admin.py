from django.contrib import admin

from src.apps.auth.models import user


admin.register(user.User)
admin.register(user.Profile)
