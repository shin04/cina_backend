from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserSerializer, WorkspaceSerializer, WorksapeTableSerializer
from .models import Workspace, WorksapeTable

class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class WorkspaceViewset(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

class WorkspaceTableViewset(viewsets.ModelViewSet):
    queryset = WorksapeTable.objects.all()
    serializer_class = WorksapeTableSerializer