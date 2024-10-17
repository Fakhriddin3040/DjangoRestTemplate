from django.contrib import admin

from .slide import SlideAdmin
from ..models import Slide


admin.site.register(Slide, SlideAdmin)
