from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Workspace, WorksapeTable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('uuid', 'username', 'email')

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('uuid', 'name')

class WorksapeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksapeTable
        fields = ('workspace', 'user')
