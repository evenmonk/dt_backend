from rest_framework import serializers
from app.internal.models.user import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_username', 'telegram_id', 'phone_number')