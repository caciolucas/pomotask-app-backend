from rest_framework import serializers

from pomotask.apps.core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
