from services.factories import ServiceFactory
from django.test import TestCase, tag


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
            service.save()
            self.assertIsNotNone(service.car_part.category.id)
            self.assertIsNotNone(service.car_part.car.engine.id)
            self.assertIsNotNone(service.car_part.car.owner.user.id)
            self.assertIsNotNone(service.car_part.car.owner.pk)
            self.assertIsNotNone(service.car_part.car.id)
            self.assertIsNotNone(service.car_part.id)
            self.assertIsNotNone(service.id)
