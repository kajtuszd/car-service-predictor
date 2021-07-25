from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Car


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


def transaction_on_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))

    return inner


@receiver(post_save, sender=Car)
@transaction_on_commit
def correct_parts_type_validator(instance, **kwargs):
    parts = instance.parts.all()
    for part in parts:
        if part.category.drive_type != '':
            if part.category.drive_type != instance.engine.engine_type:
                raise ValidationError('Invalid car drive or car part type')
