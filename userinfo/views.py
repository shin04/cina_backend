from rest_framework import status
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

    def create(self, request):
        # print(request.POST.get('admin', None))
        # print(request.data.workspace_name)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = get_user_model().objects.get(uuid=request.POST.get('admin', None))
        workspace = Workspace.objects.get(workspace_name=request.POST.get('workspace_name', None))
        relation_table = WorksapeTable(user=user, workspace=workspace, user_authority='admin')
        relation_table.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False)
    def exist_workspace(self, request):
        workspace = Workspace.objects.all().filter(workspace_name__iexact=request.GET.get("workspace_name"))
        if workspace == None:
            return Response({'exist': False})
        else:
            return Response({'exist': True})

    @action(detail=True, methods=['post'])
    def add_user(self, request, pk):
        # 追加したいユーザのメールアドレスを送る
        user = get_user_model().objects.get(email=request.data["add_user"])
        workspace = Workspace.objects.get(pk=pk)
        relation_table = WorksapeTable(user=user, workspace=workspace, user_authority='general')
        relation_table.save()

        return Response({'status': 'success'})

class WorkspaceTableViewset(viewsets.ModelViewSet):
    queryset = WorksapeTable.objects.all()
    serializer_class = WorksapeTableSerializer