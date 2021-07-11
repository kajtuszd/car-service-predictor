import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'username%d' % n)
    email = factory.LazyAttribute(lambda e: '%s@example.pl' % e.username)
    password1 = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    password2 = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = 'user.User'


class WorkshopFactory(factory.django.DjangoModelFactory):
    workshop_name = factory.Sequence(lambda n: 'workshop_name%d' % n)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = 'user.Workshop'
