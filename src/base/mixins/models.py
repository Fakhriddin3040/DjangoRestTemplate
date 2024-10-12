from django.db import models


class AbstractTimestambleModelFields:
    created_at = models.DateTimeField(verbose_name="Создано в", auto_created=True)
    updated_by = models.DateTimeField(
        verbose_name="Обновлено в", auto_now=True, null=True, blank=True
    )


class AbstractAuditModelsFields:
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Создал"
    )
    updated_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Обновил"
    )
