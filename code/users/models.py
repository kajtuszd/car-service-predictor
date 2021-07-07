from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                                            RegexValidator)


class User(AbstractUser):
    is_customer = models.BooleanField(_('Is customer'), default=False)
    is_workshop = models.BooleanField(_('Is workshop'), default=False)
    city = models.CharField(_('City'), max_length=30, null=True)
    street = models.CharField(_('Street'), max_length=30, null=True)
    house_number = models.IntegerField(_('House number'), null=True,
                                       validators=[MaxValueValidator(1000),
                                                   MinValueValidator(1)])
    flat_number = models.IntegerField(_('Flat number'), null=True, blank=True,
                                      validators=[MaxValueValidator(100),
                                                  MinValueValidator(1)])
    zip_code = models.CharField(_('Zip code'), null=True, max_length=6,
                                validators=[RegexValidator(r'^\d{2}-\d{3}$',
                                                           _('Zip code must '
                                                             'be entered in '
                                                             'the format '
                                                             '12-345.'))])


class Customer(User):
    pass


class Workshop(User):
    pass

