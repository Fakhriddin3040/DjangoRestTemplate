from typing import Any, Dict, Tuple, Union
from django.db import models
from src.base import types


class AbstractDjangoRepository(types.AbstractGenericClass[types.TModel]):
    model: types.TModel

    def get(self, pk: int) -> Union[types.TModel, None]:
        return self.model.objects.filter(pk=pk).first()

    def all(self) -> models.QuerySet[types.TModel]:
        return self.model.objects.all()

    def create(self, **kwargs) -> types.TModel:
        return self.model.objects.create(**kwargs)

    def update(self, pk: int, params: types.BaseParams) -> int:
        return self.model.objects.filter(pk=pk).update(**params.__dict__)

    def delete(self, pk: int) -> bool:
        return bool(self.model.objects.filter(pk=pk).delete())

    def get_by_lookup(self, lookup: str, value: Any) -> Union[types.TModel, None]:
        return self.model.objects.filter(**{lookup: value}).first()

    def create_or_update(
        self, defaults: Dict[str, Any], **kwargs
    ) -> Tuple[types.TModel, bool]:
        obj, created = self.model.objects.update_or_create(default=defaults, **kwargs)
        return obj, created

    def exists(self, **kwargs) -> bool:
        return self.all().filter(**kwargs).exists()

    def save(self, instance: types.TModel) -> types.TModel:
        instance.save()
        return instance
