from http import HTTPMethod
from typing import Dict
from rest_framework import serializers
from src.base import types


class SerializerContextRetrieverMixin:
    def get_serializer_context(self) -> Dict:
        return {"request": self.request, "format": self.format_kwarg, "view": self}


class ListSerializerRetrieverMixin(SerializerContextRetrieverMixin):
    list_serializer_class: serializers.Serializer = None

    def get_list_serializer(self, *args, **kwargs) -> serializers.Serializer:
        kwargs.setdefault("context", self.get_serializer_context())
        return self.list_serializer_class(
            *args,
            **kwargs,
            read_only=True,
        )


class RetrieveSerializerRetrieverMixin(SerializerContextRetrieverMixin):
    retrieve_serializer_class: serializers.Serializer = None

    def get_retrieve_serializer(self, *args, **kwargs) -> serializers.Serializer:
        kwargs.setdefault("context", self.get_serializer_context())
        return self.retrieve_serializer_class(*args, **kwargs, read_only=True)


class CreateSerializerRetrieverMixin(ListSerializerRetrieverMixin):
    create_serializer_class: serializers.Serializer = None

    def get_serializer_class(self) -> serializers.Serializer:
        if self.request.method == HTTPMethod.POST:
            return self.create_serializer_class
        return self.list_serializer_class


class UpdateSerializerRetrieverMixin(RetrieveSerializerRetrieverMixin):
    update_serializer_class: serializers.Serializer = None

    def get_serializer_class(self) -> serializers.Serializer:
        if self.request.method == HTTPMethod.PUT:
            return self.update_serializer_class
        return self.retrieve_serializer_class


class ListCreateSerializerRetrieverMixin(CreateSerializerRetrieverMixin):
    def get_serializer_class(self) -> serializers.Serializer:
        if self.request.method == HTTPMethod.GET:
            return self.list_serializer_class
        return self.create_serializer_class


class RetrieveUpdateSerializerRetrieverMixin(
    UpdateSerializerRetrieverMixin, RetrieveSerializerRetrieverMixin
):
    pass


class CRUDSerializerRetrieverMixin(
    ListCreateSerializerRetrieverMixin, RetrieveUpdateSerializerRetrieverMixin
):
    def get_serializer_class(self) -> serializers.Serializer:
        if self.request.method == HTTPMethod.GET:
            return self.list_serializer_class
        if self.action == "retrieve":
            return self.retrieve_serializer_class
        if self.request.method == HTTPMethod.POST:
            return self.create_serializer_class
        return self.update_serializer_class


#! ============================================= !#


class CreateUseCaseRetrieverMixin:
    create_use_case_class: types.BaseUseCase = None

    def get_use_case_class(self):
        return self.create_use_case_class

    def get_use_case(self, *args, **kwargs):
        return self.get_use_case_class()(*args, **kwargs)


class UpdateUseCaseRetrieverMixin:
    update_use_case_class: types.BaseUseCase = None

    def get_use_case_class(self):
        return self.update_use_case_class

    def get_use_case(self, *args, **kwargs):
        return self.get_use_case_class()(*args, **kwargs)


class CreateUpdateUseCaseMixin(
    CreateUseCaseRetrieverMixin, UpdateUseCaseRetrieverMixin
):
    def get_use_case_class(self):
        if self.method == HTTPMethod.POST:
            return self.create_use_case_class
        return self.update_use_case_class


#! ============================================= !#


class CreateParamsRetrieverMixin:
    create_params_class: types.BaseParams

    def get_params_class(self):
        return self.create_params_class

    def get_params(self, *args, **kwargs):
        return self.get_params_class()(*args, **kwargs)


class UpdateParamsRetrieverMixin:
    update_params_class: types.BaseParams

    def get_params_class(self):
        return self.update_params_class

    def get_params(self, *args, **kwargs):
        return self.get_params_class()(*args, **kwargs)


class CreateUpdateParamsMixin(CreateParamsRetrieverMixin, UpdateParamsRetrieverMixin):
    def get_params_class(self):
        if self.method == HTTPMethod.POST:
            return self.create_params_class
        return self.update_params_class
