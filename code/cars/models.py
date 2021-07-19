import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from .validators import car_brand_validator, no_future_validator, \
    no_past_validator


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


class CarPartCategory(models.Model):
    name = models.CharField(_('Part name'), max_length=30, unique=True)
    drive_type = models.CharField(_('Only for drive type'), max_length=20,
                                  choices=EngineType.TYPES, blank=True)

    class Meta:
        verbose_name = _('car part category')
        verbose_name_plural = _('car part categories')

    def __str__(self):
        return f'{self.name}'


class CarPart(models.Model):
    category = models.ForeignKey(CarPartCategory, on_delete=models.CASCADE)
    latest_fix_date = models.DateTimeField(_('Latest service date'),
                                           validators=[no_future_validator])
    latest_fix_mileage = models.PositiveIntegerField(
        _('Car mileage before latest service'),
        validators=[MinValueValidator(0), MaxValueValidator(1000000)],
    )
    fix_every_period = models.PositiveIntegerField(
        _('Service needed every - period'))
    fix_every_mileage = models.PositiveIntegerField(
        _('Service needed every - mileage'),
        validators=[MinValueValidator(0), MaxValueValidator(1000000)],
        )
    next_fix_date = models.DateTimeField(_('Next service date'),
                                         validators=[no_past_validator],
                                         blank=True, null=True)
    next_fix_mileage = models.PositiveIntegerField(
        _('Mileage until next service'),
        validators=[MinValueValidator(0), MaxValueValidator(1000000)],
        blank=True, null=True
    )
    description = models.CharField(_('Car part description'), max_length=50,
                                   blank=True, null=True)

    class Meta:
        verbose_name = _('car part')
        verbose_name_plural = _('car parts')

    def __str__(self):
        return f'{self.category}'


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
                                        'invalid'), ],
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
