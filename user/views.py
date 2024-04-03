from django.shortcuts import render

from .models import CustomUser
from .serializer import UserSerializer 

# Create your views here.
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

