from django.contrib.auth.models import User
from .models import TimeManagement
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class TimeManagementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeManagement
        fields = ['user', 'start_time']