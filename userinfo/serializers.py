from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Workspace, WorksapeTable

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('uuid', 'name', 'admin')

class WorksapeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksapeTable
        fields = ('id', 'workspace', 'user') 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('uuid', 'username', 'email')