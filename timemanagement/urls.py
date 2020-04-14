from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

router = routers.DefaultRouter()
router.register('timemanagement', TimeManagementViewSet)
