from rest_framework import serializers

from core.models import Task, TaskListElement


class TaskListElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskListElement


class TaskSerializer(serializers.ModelSerializer):
    items = TaskListElementSerializer(many=True)

    class Meta:
        model = Task

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        task = Task.objects.create(**validated_data)
        for item_data in items_data:
            TaskListElement.objects.create(task=task, **item_data)
        return task

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.is_realized = validated_data.get('is_realized', instance.is_realized)
        instance.priority = validated_data.get('priority', instance.priority)
        items = validated_data.pop('items')
        for item in items:
            try:
                obj = TaskListElement.objects.get(id=item.get('id'))
            except TaskListElement.DoesNotExist:
                obj = TaskListElement()
            obj.task = instance
            obj.checked = item.get('checked')
            obj.description = item.get('description')
            obj.save()
        instance.save()
        return instance
