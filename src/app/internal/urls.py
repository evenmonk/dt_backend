from django.urls import path, include

from app.internal.transport.rest.handlers import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'me', UserViewSet, basename='me')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include('rest_framework.urls', namespace='rest_framework'))
]
