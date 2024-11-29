from django.db import models


class MKSyncInfo(models.Model):
    cat_synced_at = models.DateTimeField(null=True)
    prod_synced_at = models.DateTimeField(null=True)
    synced_at = models.DateTimeField(null=True)
