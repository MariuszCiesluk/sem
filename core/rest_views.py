from rest_framework import generics

from core.models import Task
from core.serializers import TaskSerializer


class TaskRestListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# class TaskRestView(generics.APIView):
#     serializer = TaskSerializer

