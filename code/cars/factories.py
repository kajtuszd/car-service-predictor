import random
import string
from datetime import datetime

import factory
import factory.fuzzy
from django.utils import timezone
from users.factories import CustomerFactory

from .models import EngineType, return_current_year


class EngineFactory(factory.django.DjangoModelFactory):
    capacity = factory.fuzzy.FuzzyDecimal(0.7, 6.0, 1)
    horsepower = factory.fuzzy.FuzzyInteger(20, 1000)
    engine_type = factory.fuzzy.FuzzyChoice([i[0] for i in EngineType.TYPES])

    class Meta:
        model = 'cars.Engine'


class CarPartCategoryFactory(factory.django.DjangoModelFactory):
    car_part_categories = {'Gearbox': 'LPG',
                           'Batteries': 'Hybrid',
                           'Timing belt': '',
                           'Spark plugs': 'Petrol',
                           'Glow plugs': 'Diesel',
                           'Engine oil': ''
                           }
    name = factory.Iterator(car_part_categories.keys())
    drive_type = factory.LazyAttribute(lambda a: a.car_part_categories[a.name])

    class Meta:
        model = 'cars.CarPartCategory'
        exclude = ('car_part_categories',)


class CarFactory(factory.django.DjangoModelFactory):
    car_models = {'BMW': ['128i', '328i', 'X5', 'M6'],
                  'Volkswagen': ['Passat', 'Golf', 'Touareg', 'Jetta'],
                  'Porsche': ['911', 'Boxster', 'Cayenne', 'Cayman'],
                  'Toyota': ['Corolla', 'Land Cruiser', 'RAV4', 'Yaris'],
                  'KIA': ['Rio', 'Soul', 'Sportage', 'Optima'],
                  'Volvo': ['S60', 'V60', 'XC60', 'S80'],
                  'Jeep': ['Wrangler', 'Grand Cherokee', 'Renegade', 'Compass'],
                  }

    owner = factory.SubFactory(CustomerFactory)
    brand = factory.fuzzy.FuzzyChoice(car_models.keys())
    model = factory.LazyAttribute(
        lambda n: random.choice(n.car_models[n.brand])
    )
    production_year = factory.fuzzy.FuzzyInteger(1990, return_current_year())
    mileage = factory.fuzzy.FuzzyInteger(0, 1000000)
    engine = factory.SubFactory(EngineFactory)

    @factory.sequence
    def registration(n):
        result = []
        letters_number = random.choice([2, 3])
        numbers_number = random.choice([5, 6])
        for _ in range(letters_number):
            result.append(random.choice(string.ascii_uppercase))
        result.append(' ')
        for _ in range(numbers_number):
            result.append(random.choice(string.digits + string.ascii_uppercase))
        return ''.join(str(i) for i in result)

    class Meta:
        model = 'cars.Car'
        exclude = ('car_models',)


class CarPartFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CarPartCategoryFactory)
    latest_fix_date = factory.fuzzy.FuzzyDateTime(
        datetime(return_current_year(), 1, 1, tzinfo=timezone.now().tzinfo)
        )
    latest_fix_mileage = factory.fuzzy.FuzzyInteger(20, 1000)
    fix_every_period = factory.fuzzy.FuzzyInteger(20, 1000)
    fix_every_mileage = factory.fuzzy.FuzzyInteger(20, 1000)
    car = factory.SubFactory(CarFactory)

    @factory.lazy_attribute
    def choose_engine(self):
        if self.category.drive_type == '':
            choices = [i[0] for i in EngineType.TYPES]
            self.car.engine.engine_type = random.choice(choices)
        else:
            self.car.engine.engine_type = self.category.drive_type

    class Meta:
        model = 'cars.CarPart'
        exclude = ('choose_engine',)
