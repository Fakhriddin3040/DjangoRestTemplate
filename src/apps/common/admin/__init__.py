from django.contrib import admin

from .organization import OrganizationAdmin
from .social_media import SocialMediaAdmin
from ..models import SocialMedia, Organization


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
