from rest_framework import viewsets

from usuarios.models import Usuarios
from usuarios.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer
