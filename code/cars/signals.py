from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Car, CarPart


@receiver(pre_save, sender=Car)
def unique_registration_validator(instance, **kwargs):
    if Car.objects.filter(
            registration=instance.registration).exists() and \
            instance.registration is not None:
        if Car.objects.get(
                registration=instance.registration).id != instance.id:
            raise ValidationError(
                f'Car with registration {instance.registration} exists '
                f'in database already'
            )


@receiver(pre_save, sender=CarPart)
def correct_parts_type_validator(instance, **kwargs):
    if instance.category.drive_type != '':
        if instance.category.drive_type != instance.car.engine.engine_type:
            raise ValidationError('Invalid car drive or car part type')
