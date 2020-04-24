from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewset, WorkspaceViewset, WorkspaceTableViewset

router = DefaultRouter()
router.register('users', UserViewset)
router.register('workspaces', WorkspaceViewset)
router.register('workspacetable', WorkspaceTableViewset)