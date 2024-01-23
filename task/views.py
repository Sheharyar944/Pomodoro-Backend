from django.shortcuts import render
from rest_framework import viewsets
from task.models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        userId = self.request.query_params.get('id')
        if userId is not None:
            return Task.objects.filter(user_id=userId)
        return Task.objects.all()
    
class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all tasks
        for the user as determined by the user_id URL parameter.
        """
        user_id = self.kwargs['user_id']
        return Task.objects.filter(user__id=user_id)
    
    def post(self, request, format=None):
        return Response({"message": "POST request received"}, status=status.HTTP_200_OK)
    
 