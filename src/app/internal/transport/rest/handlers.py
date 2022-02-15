from app.internal.models.user import User
from rest_framework import viewsets
from app.internal.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username')
        self.queryset = User.objects.filter(telegram_username=username)
        return self.queryset
        