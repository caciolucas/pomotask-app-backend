from django.shortcuts import render
from rest_framework import viewsets
from pomotask.apps.core.models import Task
from pomotask.apps.core.serializers import TaskSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        # set owner to requested user
        if self.request.user.is_authenticated:
            request.data['owner'] = self.request.user.id
        return super().create(request, *args, **kwargs)