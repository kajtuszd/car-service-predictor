from datetime import date

from cars.models import CarPart
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import Workshop
from utils.slugs import generate_slug


def no_past_validator(chosen_date):
    if chosen_date < date.today():
        raise ValidationError('This cannot be done in the past.')


class Service(models.Model):
    title = models.CharField(_('Title'), max_length=30)
    cost = models.DecimalField(_('Cost'), validators=[MaxValueValidator(50000),
                                                      MinValueValidator(0)],
                               decimal_places=2, max_digits=7)
    car_part = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    date = models.DateField(_('Service date'),
                            validators=[no_past_validator],
                            blank=True, null=True)
    time = models.TimeField(_('Service time'), blank=True, null=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    days_from_latest_fix = models.PositiveIntegerField(
        _('Days from latest fix'), validators=[MaxValueValidator(10000)],
        default=0)
    mileage_from_latest_fix = models.PositiveIntegerField(
        _('Mileage from latest fix'), validators=[MaxValueValidator(1000000)],
        default=0)
    description = models.CharField(_('Description'), max_length=100, blank=True)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE,
                                 blank=False, null=True)
    slug = models.CharField(_('Slug'), default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return f'{self.title}'
