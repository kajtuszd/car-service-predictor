from __future__ import absolute_import, unicode_literals

from datetime import date, timedelta

from cars.models import Car, CarPart, CarPartCategory
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Service


@shared_task
def send_email_service_confirmation(slug):
    service = Service.objects.get(slug=slug)
    html_message = render_to_string('service_create.html', {'service': service})
    plain_message = strip_tags(html_message)
    send_mail('Service booking confirmation',
              plain_message,
              settings.DEFAULT_FROM_EMAIL,
              (service.car_part.car.owner.email,),
              html_message=html_message
              )


@shared_task
def send_email_service_update(slug):
    service = Service.objects.get(slug=slug)
    html_message = render_to_string('service_update.html', {'service': service})
    plain_message = strip_tags(html_message)
    send_mail('Booked service update',
              plain_message,
              settings.DEFAULT_FROM_EMAIL,
              (service.car_part.car.owner.email,),
              html_message=html_message
              )


def calculate_next_fix_date(car_part):
    car_part.next_fix_mileage = car_part.latest_fix_mileage + car_part.fix_every_mileage
    next_service_days = (
                                    car_part.next_fix_mileage - car_part.car.mileage) / car_part.car.daily_mileage
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


@shared_task
def update_latest_fix_data():
    services = Service.objects.all()
    for service in services:
        if service.is_active:
            service.mileage_from_latest_fix = service.car_part.car.mileage - service.car_part.latest_fix_mileage
            d_time = service.date - service.car_part.latest_fix_date
            service.days_from_latest_fix = d_time.days
            print(d_time.days)
            service.save()


@shared_task
def calculate_predicted_fix_data():
    all_car_parts = CarPart.objects.all()
    for car_part in all_car_parts:
        brand = car_part.car.brand
        model = car_part.car.model
        cars = Car.objects.filter(brand=brand, model=model)
        category = CarPartCategory.objects.get(name=car_part.category.name)
        car_parts = []
        for car in cars:
            car_parts += CarPart.objects.filter(car=car, category=category)
        services = []
        if car_parts:
            for car_part in car_parts:
                services += Service.objects.filter(car_part=car_part)
            inactive_services = []
            for service in services:
                if not service.is_active:
                    inactive_services.append(service)
            if not inactive_services:
                car_part.predicted_fix_mileage = None
                car_part.predicted_fix_date = None
                car_part.save()
            else:
                sum_days = 0
                sum_mileage = 0
                for inactive_service in inactive_services:
                    sum_days += inactive_service.days_from_latest_fix
                    sum_mileage += inactive_service.mileage_from_latest_fix
                car_part.predicted_fix_mileage = car_part.latest_fix_mileage + sum_mileage / len(
                    inactive_services)
                car_part.predicted_fix_date = car_part.latest_fix_date + timedelta(
                    days=sum_days / len(inactive_services))
                car_part.save()
        else:
            car_part.predicted_fix_mileage = None
            car_part.predicted_fix_date = None
            car_part.save()
