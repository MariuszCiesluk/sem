from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Task, TaskListElement
from core.serializers import TaskSerializer, TaskListElementSerializer


"""
Serializers for Task and TaskListElement
Inheritance from two classes:
* generics.ListCreateAPIView
* generics.RetrieveUpdateDestroyAPIView

first, for list and create views
second, for read-write operations for single object
"""


class TaskRestListView(generics.ListCreateAPIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskRestView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskListElementRestListView(generics.ListCreateAPIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListElementSerializer

    def get_queryset(self):
        return TaskListElement.objects.filter(task=self.request.GET.get('pk'))


class TaskListElementRestView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListElementSerializer

    def get_queryset(self):
        return TaskListElement.objects.filter(task=self.request.GET.get('pk'))



