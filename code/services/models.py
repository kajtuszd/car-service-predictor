from cars.models import CarPart
from cars.validators import no_past_validator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Service(models.Model):
    title = models.CharField(_('Title'), max_length=30)
    cost = models.DecimalField(_('Cost'), validators=[MaxValueValidator(50000),
                                                      MinValueValidator(0)],
                               decimal_places=2, max_digits=7)
    car_part = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    date_start = models.DateTimeField(_('Start date'),
                                      validators=[no_past_validator])
    date_finish = models.DateTimeField(_('Finish date'),
                                       validators=[no_past_validator])
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(_('Description'), max_length=100, blank=True)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return f'{self.title}'
