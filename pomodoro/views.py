from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PomodoroSerializer
from .models import Pomodoro
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class PomodoroSettingsView(APIView):
    def get(self, request, format=None):
        settings = Pomodoro.objects.all()
        serializer = PomodoroSerializer(settings, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer= PomodoroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
class PomodoroSettingsUpdateView(APIView):
    # serializer_class = PomodoroSerializer
    def get(self, request, **kwargs):
        user_id = kwargs['user_id']
        settings_name = request.query_params.get('settings_name')
        queryset = Pomodoro.objects.filter(user=user_id)
        if settings_name:
            queryset = queryset.get(settings_name=settings_name)
            serializer = PomodoroSerializer(queryset)
            return Response(serializer.data)
        
        serializer = PomodoroSerializer(queryset, many=True)
        return Response(serializer.data)

    def post (self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        settings_name = request.query_params.get('settings_name')
        queryset = Pomodoro.objects.filter(user_id=user_id)
        if settings_name:
            queryset= queryset.get(settings_name=settings_name)
        serializer = PomodoroSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        data = request.data
        instances_data = data  # Assuming data is an array of objects
        
        # Loop through each instance data and update the corresponding instance
        for instance_data in instances_data:
            instance_id = instance_data.get('id')
            if instance_id:
                try:
                    instance = Pomodoro.objects.get(id=instance_id)
                    serializer = PomodoroSerializer(instance, data=instance_data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except Pomodoro.DoesNotExist:
                    return Response({'error': f'Instance with id {instance_id} not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'Instance id not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Instances updated successfully'}, status=status.HTTP_200_OK)
    
    def delete(self, request, **kwargs):
        user_id = kwargs['user_id']
        settings_name = request.query_params.get("settings_name")
        queryset=Pomodoro.objects.filter(user_id=user_id)
        if settings_name:
            instance = queryset.get(settings_name=settings_name)
            instance.delete()
            return Response({'message': 'instance deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            

