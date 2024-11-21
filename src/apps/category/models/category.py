from django.db import models


from ..managers import category as category_manager


class Category(models.Model):
    objects = category_manager.CategoryManager()

    """External service id"""
    ext_id = models.CharField(max_length=50, unique=True)
    ext_parent_title = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    parent = models.ForeignKey(
        "category.Category",
        on_delete=models.CASCADE,
        to_field="ext_parent_title",
        null=True,
        blank=True,
    )
