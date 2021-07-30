from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Service
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=Service)
def return_date_validator(instance, **kwargs):
    if instance.date_start > instance.date_finish:
        raise ValidationError('Service start date should be before finish date.')
