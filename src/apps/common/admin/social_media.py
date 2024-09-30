from django.contrib import admin

from src.utils.functions.admin import get_image_with_tag


class SocialMediaAdmin(admin.ModelAdmin):
    def icon_tag(self, obj):
        if obj.icon:
            return get_image_with_tag(instance=obj.icon, image_field="image")
        return None

    list_display = ("title", "icon_tag", "link")
    list_display_links = ("title", "icon_tag")
