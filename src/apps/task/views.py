from typing import Type

from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, views, generics
from rest_framework.serializers import BaseSerializer

from .models import Task
from .serializers import TaskListSerializer, TaskCreateSerializer, TaskUpdateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    model = Task

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == 'create':
            return TaskCreateSerializer
        elif self.action == 'update':
            return TaskUpdateSerializer
        return TaskListSerializer

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user)
