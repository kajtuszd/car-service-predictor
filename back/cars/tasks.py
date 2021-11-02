from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import CarPart


@shared_task
def decrease_fix_mileage():
    car_parts = CarPart.objects.all()
    for car_part in car_parts:
        print("before: " + str(car_part.next_fix_mileage))
        car_part.next_fix_mileage -= 1
        car_part.save()
        print("after: " + str(car_part.next_fix_mileage))
    print("Decreased car part days until next service")
