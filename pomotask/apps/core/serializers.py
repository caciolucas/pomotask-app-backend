from django.contrib.auth.models import User
from rest_framework import serializers

from pomotask.apps.core.models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Task
        fields = '__all__'
