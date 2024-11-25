from django.db import models


class MKSyncInfo(models.Model):
    cat_synced = models.DateTimeField(null=True)
    prod_synced = models.DateTimeField(null=True)
    synced = models.DateTimeField(null=True)
