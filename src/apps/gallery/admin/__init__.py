from django.contrib import admin

from .image import ImageAdmin
from .slide import SlideAdmin
from ..models import Image, Slide


admin.site.register(Image, ImageAdmin)
admin.site.register(Slide, SlideAdmin)
