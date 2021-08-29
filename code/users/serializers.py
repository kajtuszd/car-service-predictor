from rest_framework import serializers
from .models import User, Workshop, Customer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
