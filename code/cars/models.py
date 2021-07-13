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


class Car(models.Model):
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
                                        'invalid')],
                                    max_length=10, blank=True, unique=True)
    mileage = models.PositiveIntegerField(_('Car mileage'), default=0,
                                          validators=[
                                              MinValueValidator(0),
                                              MaxValueValidator(1000000)])

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')

    def __str__(self):
        return f'{self.brand} {self.model}'
