from django.contrib import admin


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("link", "icon", "social_type")
    list_display_links = ("link",)
