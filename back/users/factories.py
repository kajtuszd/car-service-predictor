import random

import factory


class WorkshopFactory(factory.django.DjangoModelFactory):
    workshop_name = factory.Sequence(lambda n: 'workshop_name%d' % n)
    city = factory.Faker('city')
    street = factory.Sequence(lambda n: 'street%d' % n)
    house_number = factory.fuzzy.FuzzyInteger(1, 1000)
    flat_number = factory.fuzzy.FuzzyInteger(1, 100)
    email = factory.Sequence(lambda e: '%s@workshop.pl' % e)

    @factory.sequence
    def phone(n):
        result = []
        for i in range(9):
            result.append(random.randint(0,9))
        return ''.join(str(i) for i in result)        

    @factory.sequence
    def zip_code(n):
        result = []
        for _ in range(2):
            result.append(random.randint(0,9))
        result.append('-')
        for _ in range(3):
            result.append(random.randint(0,9))
        return ''.join(str(i) for i in result)

    class Meta:
        model = 'users.Workshop'


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'username%d' % n)
    email = factory.LazyAttribute(lambda e: '%s@example.pl' % e.username)
    password1 = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    password2 = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    workshop = factory.SubFactory(WorkshopFactory)

    class Meta:
        model = 'users.User'
