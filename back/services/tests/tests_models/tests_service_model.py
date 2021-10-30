from datetime import date, timedelta

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
            service.car_part.car.owner.workshop.save()
            service.car_part.car.owner.save()
            service.car_part.car.save()
            service.car_part.save()
            service.workshop.save()
            service.save()
            self.assertIsNotNone(service.car_part.category.id)
            self.assertIsNotNone(service.car_part.car.engine.id)
            self.assertIsNotNone(service.car_part.car.owner.pk)
            self.assertIsNotNone(service.car_part.car.id)
            self.assertIsNotNone(service.car_part.id)
            self.assertIsNotNone(service.car_part.car.owner.workshop.id)
            self.assertIsNotNone(service.id)


@tag('service')
class ServiceDeletionTests(TestCase):

    def setUp(self):
        self.service = ServiceFactory()

    def test_delete_service_object(self):
        self.service.delete()
        self.assertIsNotNone(self.service.car_part.category.id)
        self.assertIsNotNone(self.service.car_part.car.engine.id)
        self.assertIsNotNone(self.service.car_part.car.owner.pk)
        self.assertIsNotNone(self.service.car_part.car.id)
        self.assertIsNotNone(self.service.car_part.id)
        self.assertIsNotNone(self.service.workshop.id)
        self.assertIsNone(self.service.id)


@tag('service')
class ServiceModelTests(TestCase):

    def setUp(self):
        self.services = ServiceFactory.create_batch(3)

    def test_service_str_method(self):
        for service in self.services:
            self.assertEquals(service.__str__(), f'{service.title}')

    def test_finish_date_is_not_in_past(self):
        for service in self.services:
            self.assertGreater(service.date, date.today() - timedelta(days=1))
