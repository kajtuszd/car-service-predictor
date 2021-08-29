from rest_framework import serializers

from .models import Car, CarPart, CarPartCategory, Engine


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPartCategory
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPart
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
