from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from services.factories import ServiceFactory


@tag('service')
class ServiceCreationTests(TestCase):

    def setUp(self):
        self.services = ServiceFactory.build_batch(5)

    def test_save_service_object(self):
        for service in self.services:
            service.car_part.category.save()
            service.car_part.car.engine.save()
            service.car_part.car.owner.user.save()
            service.car_part.car.owner.save()
            service.car_part.car.save()
            service.car_part.save()
            service.workshop.user.save()
            service.workshop.save()
            service.save()
            self.assertIsNotNone(service.car_part.category.id)
            self.assertIsNotNone(service.car_part.car.engine.id)
            self.assertIsNotNone(service.car_part.car.owner.user.id)
            self.assertIsNotNone(service.car_part.car.owner.pk)
            self.assertIsNotNone(service.car_part.car.id)
            self.assertIsNotNone(service.car_part.id)
            self.assertIsNotNone(service.workshop.user.id)
            self.assertIsNotNone(service.workshop.pk)
            self.assertIsNotNone(service.id)


@tag('service')
class ServiceDeletionTests(TestCase):

    def setUp(self):
        self.service = ServiceFactory()

    def test_delete_service_object(self):
        self.service.delete()
        self.assertIsNotNone(self.service.car_part.category.id)
        self.assertIsNotNone(self.service.car_part.car.engine.id)
        self.assertIsNotNone(self.service.car_part.car.owner.user.id)
        self.assertIsNotNone(self.service.car_part.car.owner.pk)
        self.assertIsNotNone(self.service.car_part.car.id)
        self.assertIsNotNone(self.service.car_part.id)
        self.assertIsNotNone(self.service.workshop.user.id)
        self.assertIsNotNone(self.service.workshop.pk)
        self.assertIsNone(self.service.id)


@tag('service')
class ServiceModelTests(TestCase):

    def setUp(self):
        self.services = ServiceFactory.create_batch(3)

    def test_service_str_method(self):
        for service in self.services:
            self.assertEquals(service.__str__(), f'{service.title}')

    def test_finish_date_is_after_start_date(self):
        for service in self.services:
            self.assertGreater(service.date_finish, service.date_start)

    def test_finish_date_is_before_start_date(self):
        for service in self.services:
            service.date_finish = service.date_start - timedelta(hours=1)
            with self.assertRaises(ValidationError,
                                   msg='Service start date should be before '
                                       'finish date.'):
                service.save()
