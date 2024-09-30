from django.contrib import admin

from src.utils.functions.admin import get_image_with_tag


class OrganizationAdmin(admin.ModelAdmin):
    def icon_tag(self, obj):
        if obj.icon:
            return get_image_with_tag(instance=obj.icon, image_field="image")

    icon_tag.short_description = "Иконка Организации"

    list_display = ("title", "icon_tag", "email", "phone", "about_us")
    list_display_links = ("title", "icon_tag", "email")
