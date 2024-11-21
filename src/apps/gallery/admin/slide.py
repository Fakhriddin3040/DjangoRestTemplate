from django.contrib import admin
from django.db import models
from src.utils.data_structures.linked_list_queu import LinkedListQueue
from src.apps.gallery.models.slide import Slide

from src.apps.gallery.utils import add_end_queue


class SlideAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = LinkedListQueue()

    def save_model(self, request, obj, form, change):
        max_turn = Slide.objects.aggregate(max_turn=models.Max("turn"))["max_turn"] or 0
        max_count = Slide.objects.count()

        if obj.turn is not None and obj.turn <= 0:
            obj.turn = 1

        if not change:
            if obj.turn is None:
                obj.turn = max_turn + 1
            elif obj.turn > max_turn + 1:
                obj.turn = max_turn + 1
            else:
                for slide in Slide.objects.filter(turn__gte=obj.turn):
                    self.queue.enqueue(slide)
                while not self.queue.is_empty():
                    slide = self.queue.dequeue()
                    slide.turn += 1
                    slide.save()

        else:
            old_turn = Slide.objects.get(pk=obj.pk).turn
            if old_turn != obj.turn:
                if obj.turn < old_turn:
                    for slide in Slide.objects.filter(
                        turn__gte=obj.turn, turn__lt=old_turn
                    ):
                        self.queue.enqueue(slide)
                    while not self.queue.is_empty():
                        slide = self.queue.dequeue()
                        slide.turn += 1
                        slide.save()
                elif obj.turn > old_turn:
                    if obj.turn > max_turn + 1:
                        obj.turn = max_count
                    for slide in Slide.objects.filter(
                        turn__gt=old_turn, turn__lte=obj.turn
                    ):
                        self.queue.enqueue(slide)
                    while not self.queue.is_empty():
                        slide = self.queue.dequeue()
                        slide.turn -= 1
                        slide.save()

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj_turn = obj.turn
        Slide.objects.filter(turn__gt=obj_turn).update(turn=models.F("turn") - 1)
        super().delete_model(request, obj)

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
