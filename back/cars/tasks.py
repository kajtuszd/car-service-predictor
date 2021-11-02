from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import CarPart, Car


@shared_task
def decrease_fix_mileage():
    car_parts = CarPart.objects.all()
    for car_part in car_parts:
        if car_part.next_fix_mileage - car_part.car.daily_mileage < 0:
            car_part.next_fix_mileage = 0
        else:
            car_part.next_fix_mileage -= car_part.car.daily_mileage
        car_part.save()


@shared_task
def update_cars_mileage():
    cars = Car.objects.all()
    for car in cars:
        if car.mileage + car.daily_mileage > 1000000:
            car.mileage = 1000000
        else:
            car.mileage += car.daily_mileage
        car.save()
