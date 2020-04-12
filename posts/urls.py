from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewset, PostViewSet

router = DefaultRouter()
router.register('users', UserViewset)
router.register('posts', PostViewSet)