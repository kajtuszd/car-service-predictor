from datetime import datetime, timedelta

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Service
from .tasks import update_service


@receiver(pre_save, sender=Service)
def set_up_service_task(instance, **kwargs):
    d_seconds = instance.time.second - datetime.now().second
    service_datetime = datetime.utcnow() + timedelta(seconds=d_seconds)
    update_service.apply_async(eta=service_datetime)
