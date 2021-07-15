import factory
import factory.fuzzy
import random
import string

from users.factories import CustomerFactory
from .models import EngineType, return_current_year


class EngineFactory(factory.django.DjangoModelFactory):
    capacity = factory.fuzzy.FuzzyDecimal(0.7, 6.0, 1)
    horsepower = factory.fuzzy.FuzzyInteger(20, 1000)
    engine_type = factory.fuzzy.FuzzyChoice(EngineType.TYPES[0])

    class Meta:
        model = 'cars.Engine'


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
        lambda n: random.choice(n.car_models[n.brand]))
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
