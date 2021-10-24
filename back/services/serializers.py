from cars.serializers import CarPartSerializer
from rest_framework import serializers
from users.serializers import WorkshopSerializer

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    car_part = CarPartSerializer()
    workshop = WorkshopSerializer()

    class Meta:
        model = Service
        fields = [
            'title',
            'cost',
            'car_part',
            'date_start',
            'date_finish',
            'is_active',
            'created_at',
            'updated_at',
            'description',
            'workshop',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
