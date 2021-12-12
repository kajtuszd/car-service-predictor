from datetime import datetime, timedelta

from cars.serializers import CarPartSerializer
from rest_framework import serializers
from users.serializers import WorkshopSerializer

from .models import Service
from .tasks import (send_email_service_confirmation, send_email_service_update,
                    update_service)


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

    @staticmethod
    def set_up_service_task(instance):
        if instance.is_active:
            d_seconds = instance.time.second - datetime.now().second
            d_minutes = instance.time.minute - datetime.now().minute
            d_hours = instance.time.hour - datetime.now().hour
            d_date = instance.date - datetime.now().date()
            service_datetime = datetime.utcnow() + timedelta(seconds=d_seconds,
                                                             minutes=d_minutes,
                                                             hours=d_hours,
                                                             days=d_date.days)
            update_service.apply_async(eta=service_datetime,
                                       kwargs={'slug': instance.slug})

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
        self.set_up_service_task(service)
        send_email_service_confirmation(service.slug)
        return service

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        send_email_service_update(instance.slug)
        return instance
