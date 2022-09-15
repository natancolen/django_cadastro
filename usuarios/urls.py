from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet

app_name = 'usuarios'

router = routers.DefaultRouter()

router.register('usuario', UserViewSet, basename="usuario")

urlpatterns = [
    path('', include(router.urls)),
]