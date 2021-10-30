import random
from datetime import timedelta, date

import factory
import factory.fuzzy
from cars.factories import CarPartFactory
from users.factories import WorkshopFactory


class ServiceFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'title%d' % n)
    cost = factory.fuzzy.FuzzyDecimal(0, 50000, 2)
    car_part = factory.SubFactory(CarPartFactory)
    date = factory.fuzzy.FuzzyDate(
        date.today() + timedelta(days=2),
        date.today() + timedelta(days=random.randint(2,32))
    )
    time = factory.Faker('time')
    is_active = factory.fuzzy.FuzzyChoice([True, False])
    description = factory.Sequence(lambda n: 'description%d' % n)
    workshop = factory.SubFactory(WorkshopFactory)

    class Meta:
        model = 'services.Service'
