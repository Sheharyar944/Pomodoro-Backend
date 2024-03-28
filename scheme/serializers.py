from rest_framework import serializers
from scheme.models import Scheme

class SchemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scheme
        fields = ['name', 'pomodoro', 'short_break', 'long_break']
