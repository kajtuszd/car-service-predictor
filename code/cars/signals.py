from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Car


@receiver(pre_save, sender=Car)
def unique_registration_validator(instance, **kwargs):
    if Car.objects.filter(registration=instance.registration).exists():
        if Car.objects.get(
                registration=instance.registration).id != instance.id:
            raise ValidationError(
                f'Car with registration {instance.registration} exists '
                f'in database already'
            )
