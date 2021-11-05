from __future__ import absolute_import, unicode_literals

from datetime import date, timedelta

from celery import shared_task

from .models import Service


def calculate_next_fix_date(car_part):
    car_part.next_fix_mileage = car_part.car.mileage + car_part.fix_every_mileage
    next_service_days = car_part.next_fix_mileage / car_part.car.daily_mileage
    next_fix_date1 = date.today() + timedelta(days=next_service_days)
    next_fix_date2 = car_part.latest_fix_date + timedelta(
        days=car_part.fix_every_period)
    if next_fix_date1 < car_part.next_fix_date or next_fix_date2 < car_part.next_fix_date:
        car_part.next_fix_date = date.today()
    else:
        if next_fix_date1 < next_fix_date2:
            car_part.next_fix_date = next_fix_date1
        else:
            car_part.next_fix_date = next_fix_date2
    car_part.car.save()
    car_part.save()


@shared_task
def update_service(slug):
    service = Service.objects.get(slug=slug)
    service.car_part.latest_fix_date = service.date
    service.car_part.latest_fix_mileage = service.car_part.car.mileage
    service.is_active = False
    service.car_part.save()
    calculate_next_fix_date(service.car_part)
    service.save()
