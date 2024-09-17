from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar
from django.db import models

T = TypeVar("T")
TModel = TypeVar("TModel", bound=models.Model)


class AbstractGenericClass(ABC, Generic[T]):
    pass


@dataclass
class BaseParams:
    pass


class BaseUseCase:
    _service = None

    def execute(self, params: BaseParams, **kwargs) -> T:
        raise NotImplementedError
