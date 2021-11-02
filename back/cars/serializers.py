from rest_framework import serializers
from users.serializers import UserSerializerDB

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
            'id',
        ]
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class CarSerializer(serializers.ModelSerializer):
    engine = EngineSerializer()
    owner = UserSerializerDB(required=False)

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
            'daily_mileage',
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

    def update(self, instance, validated_data):
        instance.registration = validated_data.get('registration',
                                                   instance.registration)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.daily_mileage = validated_data.get('daily_mileage',
                                                    instance.daily_mileage)
        instance.save()
        return instance


class CarPartSerializer(serializers.ModelSerializer):
    category = CarPartCategorySerializer()
    car = CarSerializer(required=False)

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

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = CarPartCategory.objects.get(name=category_data['name'],
                                               drive_type=category_data[
                                                   'drive_type'])
        car_part = CarPart.objects.create(category=category, **validated_data)
        return car_part

    def update(self, instance, validated_data):
        instance.latest_fix_date = validated_data.get('latest_fix_date',
                                                      instance.latest_fix_date)
        instance.latest_fix_mileage = validated_data.get('latest_fix_mileage',
                                                         instance.latest_fix_mileage)
        instance.fix_every_period = validated_data.get('fix_every_period',
                                                       instance.fix_every_period)
        instance.fix_every_mileage = validated_data.get('fix_every_mileage',
                                                        instance.fix_every_mileage)
        instance.next_fix_date = validated_data.get('next_fix_date',
                                                    instance.next_fix_date)
        instance.next_fix_mileage = validated_data.get('next_fix_mileage',
                                                       instance.next_fix_mileage)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        return instance
