from rest_framework import serializers

from .models import User, Workshop


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'
        lookup_field = 'user'
        extra_kwargs = {
            'url': {'lookup_field': 'user'}
        }
