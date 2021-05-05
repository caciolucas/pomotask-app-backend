from django.shortcuts import render
from rest_framework import viewsets
from pomotask.apps.core.models import Task
from pomotask.apps.core.serializers import TaskSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
