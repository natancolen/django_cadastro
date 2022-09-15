from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'usuarios'

router = routers.DefaultRouter()

router.register('usuarios', views, basename="index")

urlpatterns = [
    path('', include(router.urls)),
]