from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Task
        fields = ["id", 'description', 'user', 'category', 'created_at', 'updated_at', 'assigned_pomodoros', 'remaining_pomodoros']

class CreateTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['description','user']