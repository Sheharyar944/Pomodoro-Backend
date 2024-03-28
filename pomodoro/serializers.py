from .models import Pomodoro
from rest_framework import serializers

class PomodoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pomodoro
        fields = '__all__'
