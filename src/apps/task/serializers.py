from rest_framework import serializers

from src.apps.todo_list.models import Task


class CurrentUserDefault:
    def __call__(self):
        return self.context['request'].user # noqa


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "completed",
            "created_at",
            "updated_at",
        )

class TaskCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "owner"
        )

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "completed",
        )