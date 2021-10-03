from django.contrib.auth.models import AbstractUser
from django.core.validators import (EmailValidator, MaxValueValidator,
                                    MinValueValidator, RegexValidator)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.slugs import generate_slug


class Workshop(models.Model):
    workshop_name = models.CharField(_('Workshop name'), max_length=30,
                                     unique=True, null=True)
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
    slug = models.CharField(_('Slug'), default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')

    def __str__(self):
        return f'{self.workshop_name}'


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)
    phone = models.CharField(_('Phone number'), unique=True, null=True,
                             max_length=15, validators=[
            RegexValidator(r'^\+?1?\d{9,15}$', _('Phone number must be '
                                                 'entered in the format: '
                                                 '123456789 or +48123456789. '
                                                 'Up to 15 digits allowed.'))])
    email = models.CharField(_('Email address'), max_length=30, unique=True,
                             validators=[EmailValidator(
                                 message='Please enter valid E-mail address')])
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
    workshop = models.OneToOneField(Workshop, on_delete=models.CASCADE,
                                    blank=True, null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
