from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

timemanagement_list = TimeManagementViewSet.as_view({
    'get': 'list',
    'put': 'create'
})

timemanagement_detail = TimeManagementViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

timemanagement_update_finish = TimeManagementViewSet.as_view({
    'post': 'update_finish_time'
})

router = routers.DefaultRouter()
router.register('users1', UserViewSet)
router.register('timemanagement', TimeManagementViewSet)

urlpatterns = format_suffix_patterns([
    path('timemanagement_list/', timemanagement_list, name='timemanagement-list'),
    path('timemanagement_detail/<int:pk>', timemanagement_detail, name='timemanagement-detail'),
    path('timemanagement_update_finish', timemanagement_update_finish, name='timemanagement-update-finish')
])
