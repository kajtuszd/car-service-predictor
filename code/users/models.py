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

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Workshop(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

