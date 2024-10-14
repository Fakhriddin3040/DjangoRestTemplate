from typing import List, Union
from dataclasses import asdict
from django.db.models import QuerySet
from src.base import types
from src.base.abstractions.repositories import base_django_repository as django_repo


class AbstractService(types.AbstractGenericClass[types.TModel]):
    def __init__(self, repository: django_repo.AbstractDjangoRepository) -> None:
        self._repository = repository

    @property
    def model(self) -> types.TModel:
        return self._repository.model

    def get_all(self) -> List[types.TModel]:
        return list(self._repository.all())

    def get(self, pk: int) -> Union[types.TModel, None]:
        return self._repository.get(pk=pk)

    def create(self, params: types.BaseParams) -> types.TModel:
        return self._repository.create(**asdict(params))

    def update(self, pk: int, params: types.BaseParams) -> int:
        return self._repository.update(
            pk=pk,
            params={
                key: value for key, value in asdict(params).items() if value is not None
            },
        )

    def delete(self, pk: int) -> None:
        _ = self._repository.delete(pk=pk)

    def get_by_lookup(self, lookup: str, value: str) -> Union[types.TModel, None]:
        return self._repository.get_by_lookup(lookup=lookup, value=value)

    def get_queryset(self) -> Union[QuerySet[types.TModel], None]:
        return self._repository.all()

    def filter(self, **kwargs) -> Union[QuerySet[types.TModel], None]:
        return self.model.objects.filter(**kwargs)

    def exists(self, **kwargs) -> bool:
        return self._repository.exists(**kwargs)

    def save(self, instance: types.TModel) -> types.TModel:
        instance.save()
        return instance
