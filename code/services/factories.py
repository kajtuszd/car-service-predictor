import random
from datetime import datetime, timedelta

import factory
import factory.fuzzy
from cars.factories import CarPartFactory
from cars.models import return_current_year
from django.utils import timezone
from users.factories import WorkshopFactory


class ServiceFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'title%d' % n)
    cost = factory.fuzzy.FuzzyDecimal(0, 50000, 2)
    car_part = factory.SubFactory(CarPartFactory)
    date_start = factory.fuzzy.FuzzyDateTime(
        datetime(return_current_year(), 1, 1, tzinfo=timezone.now().tzinfo),
        datetime(return_current_year() + 1, 1, 1, tzinfo=timezone.now().tzinfo)
    )
    is_active = factory.fuzzy.FuzzyChoice([True, False])
    description = factory.Sequence(lambda n: 'description%d' % n)
    workshop = factory.SubFactory(WorkshopFactory)

    @factory.lazy_attribute
    def date_finish(self):
        return self.date_start + timedelta(
                minutes=random.randrange(10, 120, 10)
            )

    class Meta:
        model = 'services.Service'
