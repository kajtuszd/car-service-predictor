from __future__ import absolute_import, unicode_literals
from datetime import timedelta, date

from celery import shared_task
from cars.models import CarPart, Car
from .models import Service


@shared_task
def update_service():
    print("hello")
