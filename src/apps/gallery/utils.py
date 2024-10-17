from django.db import models
from src.apps.gallery.models.slide import Slide

def add_end_queue(obj):
    max_turn = Slide.objects.filter(turn__isnull=False).aggregate(max_turn=models.Max('turn'))['max_turn'] or 0
    if obj.turn is None or obj.turn < 0:
        obj.turn = max_turn + 1
