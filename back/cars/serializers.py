from rest_framework import serializers

from .models import Car, CarPart, CarPartCategory, Engine


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = [
            'capacity',
            'horsepower',
            'engine_type',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CarPartCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPartCategory
        fields = [
            'name',
            'drive_type',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPart
        fields = [
            'category',
            'latest_fix_date',
            'latest_fix_mileage',
            'fix_every_period',
            'fix_every_mileage',
            'next_fix_date',
            'next_fix_mileage',
            'description',
            'car',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
        )
    engine = EngineSerializer()

    class Meta:
        model = Car
        fields = [
            'owner',
            'brand',
            'model',
            'production_year',
            'registration',
            'mileage',
            'engine',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def create(self, validated_data):
        engine_data = validated_data.pop('engine')
        engine = Engine.objects.create(**engine_data)
        car = Car.objects.create(engine=engine, **validated_data)
        return car
