from django.contrib.admin import ModelAdmin


class ProductAdmin(ModelAdmin):
    list_display = ("id", "title", "price", "display_category", "count")
    list_display_links = ("id", "title")
    readonly_fields = ("ext_id", "ext_cat_id", "category", "count")
    search_fields = ("title",)
    list_filter = ("category",)

    def display_category(self, obj):
        return obj.category.title if obj.category else "-"

    display_category.short_description = "Категория"
