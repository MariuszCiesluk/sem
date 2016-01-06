from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Task
from core.serializers import TaskSerializer


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



