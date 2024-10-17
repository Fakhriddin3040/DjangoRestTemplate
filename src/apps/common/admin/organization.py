from django.contrib import admin

from src.apps.common.models.organization import Organization
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "phone", "about_us")
    list_display_links = ("title", "email")

    def has_add_permission(self, request):
        if Organization.objects.exists():
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return True
