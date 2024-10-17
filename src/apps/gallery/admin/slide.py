from django.contrib import admin
from django.db import models
from src.apps.gallery.models.slide import Slide
from src.apps.gallery.utils import add_end_queue


class SlideAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        max_turn = Slide.objects.aggregate(max_turn=models.Max("turn"))["max_turn"]
        if obj.turn is None and not change:
            if max_turn is None:
                max_turn = 0
            obj.turn = max_turn + 1
        if obj.turn < 0:
            add_end_queue(obj)

        existing_slides = Slide.objects.filter(turn__gte=obj.turn).order_by("turn")
        if existing_slides.exists():
            for slide in existing_slides:
                slide.turn += 1
                slide.save()

        if obj.turn > max_turn:
            obj.turn = max_turn + 1

        super().save_model(request, obj, form, change)

    list_display = ("title", "description", "turn", "link", "is_active")
    list_display_links = ("title",)

    actions = ["activate_slides", "deactivate_slides"]

    @admin.action(description="Активировать выбранные слайды")
    def activate_slides(self, request, queryset):
        for obj in queryset:
            add_end_queue(obj)
            obj.save()
        queryset.update(is_active=True)

    @admin.action(description="Деактивировать выбранные слайды")
    def deactivate_slides(self, request, queryset):
        queryset.update(is_active=False, turn=None)

        active_slides = Slide.objects.filter(is_active=True).order_by("turn")
        for i, slide in enumerate(active_slides, start=1):
            slide.turn = i
            slide.save()
