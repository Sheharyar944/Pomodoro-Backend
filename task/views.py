from django.shortcuts import render
from task.models import Task
from .serializers import TaskSerializer, CreateTaskSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404



# Create your views here.

# class TaskViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         userId = self.request.query_params.get('id')
#         if userId is not None:
#             return Task.objects.filter(user_id=userId)
#         return Task.objects.all()

class TaskList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None, **kwargs):
        tasks = Task.objects.all()
        task_id = request.query_params.get('id')
        if task_id:
            instance = tasks.get(id=task_id)
            serializer = TaskSerializer(instance)
            return Response(serializer.data)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_id = self.request.query_params.get('id')
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        # Set the user field before saving
        serializer.save(user=self.request.user)
    
class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(user__id=user_id)
    
    def post(self, request, user_id, format=None):
    
        task_data = request.data
        # task_data['user_id'] = user_id
        # user_instance = User.objects.get(pk=user_id)
        # task_data['user_id'] = user_instance
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response({"message": "Task created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": task_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks= Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            # serializer.save()  # Assuming user is authenticated
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        # Set the user field before saving
        serializer.save(user=self.request.user)

    def delete(self, request, user_id, task_id, format=None):
        task = get_object_or_404(Task, id=task_id, user_id=user_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, user_id, task_id, format=None):
        task= get_object_or_404(Task, id=task_id, user_id=user_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
