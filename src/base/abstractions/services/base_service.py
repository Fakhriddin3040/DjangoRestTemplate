from typing import Dict, List
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

    def get(self, pk: int) -> types.TModel:
        return self._repository.get(pk=pk)

    def create(self, params: types.BaseParams) -> types.TModel:
        return self._repository.create(params=params)

    def update(self, pk: int, data: Dict) -> int:
        return self._repository.update(pk=pk, data=data)

    def delete(self, pk: int) -> None:
        _ = self._repository.delete(pk=pk)

    def get_by_lookup(self, lookup: str, value: str) -> types.TModel:
        return self._repository.get_by_lookup(lookup=lookup, value=value)

    def get_queryset(self) -> types.TModel:
        return self._repository.all()

    def save(self, instance: types.TModel) -> types.TModel:
        instance.save()
        return instance
