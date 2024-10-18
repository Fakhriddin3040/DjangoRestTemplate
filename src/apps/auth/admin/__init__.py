from django.contrib import admin
from src.apps.auth.admin.users import UserAdmin
from src.apps.auth.models.user import User

admin.site.register(User, UserAdmin)
