from .validators import car_brand_validator, unique_registration_validator
import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)


def return_current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(return_current_year())(value)


class EngineType():
    TYPES = (
        ('Petrol', _('Petrol')),
        ('Diesel', _('Diesel')),
        ('Hybrid', _('Hybrid')),
        ('LPG', _('LPG')),
    )


class Engine(models.Model):
    capacity = models.DecimalField(_('Capacity'), default=2.0, max_digits=4,
                                   validators=[MaxValueValidator(6.0),
                                               MinValueValidator(0.7)],
                                   decimal_places=2, blank=False)
    horsepower = models.IntegerField(_('Horsepower'), blank=False, default=100,
                                     validators=[MaxValueValidator(1000),
                                                 MinValueValidator(20)])
    engine_type = models.CharField(_('Engine type'), max_length=20,
                                   choices=EngineType.TYPES)

    class Meta:
        verbose_name = _('engine')
        verbose_name_plural = _('engines')

    def __str__(self):
        return f'{self.engine_type} {self.horsepower}HP {self.capacity}'


class Car(models.Model):
    owner = models.ForeignKey('users.Customer', on_delete=models.CASCADE,
                              blank=False, null=True)
    brand = models.CharField(_('Brand'), max_length=30, blank=False)
    model = models.CharField(_('Model'), max_length=30, blank=False)
    production_year = models.PositiveIntegerField(_('Production year'),
                                                  default=return_current_year(),
                                                  validators=[
                                                      MinValueValidator(1990),
                                                      max_value_current_year])
    registration = models.CharField(_('Registration'),
                                    validators=[RegexValidator(
                                        r'^[A-Z]{2,3}[\s]{1}[0-9A-Z]{5,6}$',
                                        _("Please enter 2-3 letters, "
                                          "whitespace and 5-6 signs"),
                                        'invalid'),
                                        unique_registration_validator],
                                    max_length=10, blank=True, null=True)
    mileage = models.PositiveIntegerField(_('Car mileage'), default=0,
                                          validators=[
                                              MinValueValidator(0),
                                              MaxValueValidator(1000000)])
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, null=True,
                               blank=False)

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def save(self, *args, **kwargs):
        self.brand, self.model = car_brand_validator(self.brand, self.model)
        super(Car, self).save(*args, **kwargs)
