from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, WorkspaceSerializer, WorksapeTableSerializer
from .models import Workspace, WorksapeTable

class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class WorkspaceViewset(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    @action(detail=False)
    def exist_workspace(self, request):
        workspace = Workspace.objects.all().filter(uuid__iexact=request.GET.get(id))
        if workspace == None:
            return Response({'exist': False})
        else:
            return Response({'exist': True})

class WorkspaceTableViewset(viewsets.ModelViewSet):
    queryset = WorksapeTable.objects.all()
    serializer_class = WorksapeTableSerializer