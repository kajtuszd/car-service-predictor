from cars.serializers import CarPartSerializer
from rest_framework import serializers
from users.serializers import WorkshopSerializer

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    car_part = CarPartSerializer(required=False)
    workshop = WorkshopSerializer(required=False)

    class Meta:
        model = Service
        fields = [
            'title',
            'cost',
            'car_part',
            'date',
            'time',
            'is_active',
            'created_at',
            'updated_at',
            'description',
            'workshop',
            'days_from_latest_fix',
            'mileage_from_latest_fix',
            'slug',
        ]
        lookup_field = 'slug'
        optional_fields = [
            'days_from_latest_fix',
            'mileage_from_latest_fix',
        ]
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def create(self, validated_data):
        car_part = validated_data.pop('car_part')
        service_date = validated_data.pop('date')
        d_days = service_date - car_part.latest_fix_date
        d_mileage = car_part.car.mileage - car_part.latest_fix_mileage
        service = Service.objects.create(car_part=car_part,
                                         days_from_latest_fix=d_days.days,
                                         mileage_from_latest_fix=d_mileage,
                                         date=service_date,
                                         **validated_data)
        return service
