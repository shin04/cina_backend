from django.shortcuts import render
from django.contrib.auth.models import User
from .models import TimeManagement
from .serializers import UserSerializer, TimeManagementSerializer
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import renderers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TimeManagementViewSet(viewsets.ModelViewSet):
    queryset = TimeManagement.objects.all()
    serializer_class = TimeManagementSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def update_finish_time(self, request, pk):
        timemanagement = TimeManagement.objects.get(pk=pk)
        timemanagement.finish_work()
        timemanagement.save()
        serializer = TimeManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, sutatus=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

