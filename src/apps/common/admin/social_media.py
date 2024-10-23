from django.contrib import admin


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("link", "social_type")
    list_display_links = ("link",)
