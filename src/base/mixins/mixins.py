from typing import Dict
from django.db import models

from rest_framework.response import Response
from rest_framework import status

from src.base import function_mixins


class ListModelMixin(function_mixins.ListSerializerRetrieverMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_list_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveModelMixin(function_mixins.RetrieveSerializerRetrieverMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_retrieve_serializer(instance)
        return Response(serializer.data)


class CreateModelMixin(function_mixins.CreateSerializerRetrieverMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        serializer = self.get_list_serializer(instance)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_create(self, serializer):
        return serializer.save()


class UpdateModelMixin(function_mixins.UpdateSerializerRetrieverMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)
        serializer = self.get_retrieve_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        return serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin:
    def destroy(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance: models.Model):
        instance.delete()


#! ================================== #!
#! UseCases Based views


class UseCaseCreateModelMixin(
    function_mixins.CreateUseCaseRetrieverMixin,
    function_mixins.CreateParamsRetrieverMixin,
    function_mixins.CreateSerializerRetrieverMixin,
):
    def perform_create(self, request, **data: Dict):
        params = self.get_params(**data)
        return self.get_use_case().execute(request=request, params=params)

    def create(self, request, *args, **kwargs):
        instance = self.perform_create(request=request, **request.data)
        serializer = self.get_list_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UseCaseUpdateModelMixin(
    function_mixins.UpdateUseCaseRetrieverMixin,
    function_mixins.UpdateParamsRetrieverMixin,
):
    def perform_update(self, **data: Dict):
        lookup_arg = {self.lookup_field: self.kwargs[self.lookup_field]}
        params = self.get_params(**data)
        return self.get_use_case().execute(params=params, **lookup_arg)

    def update(self, request, *args, **kwargs):
        instance = self.perform_update(**request.data)
        serializer = self.get_retrieve_serializer(instance)
        return Response(serializer.data)


class ListUseCaseCreateModelMixin(ListModelMixin, UseCaseCreateModelMixin):
    pass


class RetrieveUseCaseUpdateDeleteModelMixin(
    UseCaseUpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
):
    pass


class UseCaseCRUDModelMixin(
    ListModelMixin,
    RetrieveModelMixin,
    UseCaseCreateModelMixin,
    UseCaseUpdateModelMixin,
    DestroyModelMixin,
):
    pass
