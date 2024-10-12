from django.contrib import admin

from src.utils.functions.admin import get_image_with_tag


class SlideAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return get_image_with_tag(instance=obj.image, image_field="image")

    list_display = ("title", "image_tag", "turn")
    list_display_links = (
        "title",
        "image_tag",
    )
