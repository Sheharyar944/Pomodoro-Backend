from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Task
        fields = ["id", 'description', 'user']

class CreateTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['description','user']