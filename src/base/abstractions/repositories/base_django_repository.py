from typing import Union
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
        return self.model.objects.filter(pk=pk).update(**params.dict())

    def delete(self, pk: int) -> bool:
        return bool(self.model.objects.filter(pk=pk).delete())

    def get_by_lookup(self, lookup: str, value: str) -> Union[types.TModel, None]:
        return self.model.objects.get(**{lookup: value})

    def save(self, instance: types.TModel) -> types.TModel:
        instance.save()
        return instance
