from datetime import datetime, timedelta

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Service
from .tasks import update_service


@receiver(pre_save, sender=Service)
def set_up_service_task(instance, **kwargs):
    d_seconds = instance.time.second - datetime.now().second
    d_minutes = instance.time.minute - datetime.now().minute
    d_hours = instance.time.hour - datetime.now().hour
    d_date = instance.date - datetime.now().date()
    service_datetime = datetime.utcnow() + timedelta(
        seconds=d_seconds, minutes=d_minutes, hours=d_hours, days=d_date.days
        )
    update_service.apply_async(eta=service_datetime)
