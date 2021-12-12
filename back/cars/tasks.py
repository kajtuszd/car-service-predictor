from __future__ import absolute_import, unicode_literals
from datetime import timedelta, date

from celery import shared_task
from .models import CarPart, Car


@shared_task
def update_cars_mileage():
    """ Adds daily mileage to general car mileage """
    cars = Car.objects.all()
    for car in cars:
        if car.mileage + car.daily_mileage > 1000000:
            car.mileage = 1000000
        else:
            car.mileage += car.daily_mileage
        car.save()


@shared_task
def calculate_next_fix_date():
    """
    Calculates estimated next fix date from:
    1. How many days are left from mileage until nextfix divided by daily mileage
    2. How many days are left from periodical fix time
    From above cases, chooses closer date
    """
    car_parts = CarPart.objects.all()
    for car_part in car_parts:

        # 1 case
        days_until_service_needed = (car_part.next_fix_mileage
                                     - car_part.car.mileage) / car_part.car.daily_mileage
        # print("\n\n1 Days until fix " + str(days_until_service_needed) + "\n\n")

        next_fix_date1 = date.today() + timedelta(days=days_until_service_needed)
        # print("date " + str(next_fix_date1) + "\n\n")

        # 2 case
        next_fix_date2 = car_part.latest_fix_date + timedelta(days=car_part.fix_every_period)
        # print("\n\n2 Days until fix" + str(next_fix_date2) + "\n\n")

        if next_fix_date1 < car_part.next_fix_date or next_fix_date2 < car_part.next_fix_date:
            car_part.next_fix_date = date.today()
        else:
            if next_fix_date1 < next_fix_date2:
                car_part.next_fix_date = next_fix_date1
            else:
                car_part.next_fix_date = next_fix_date2

        car_part.save()
