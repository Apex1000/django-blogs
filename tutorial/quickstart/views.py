from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UsersSerializer
from .models import Users


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('name')
    serializer_class = UsersSerializer