from django.test import TestCase
from cars.factories import CarFactory


class CarCreationTests(TestCase):

    def setUp(self):
        self.cars = CarFactory.build_batch(3)

    def test_save_car_object(self):
        for car in self.cars:
            car.owner.user.save()
            car.owner.save()
            car.engine.save()
            car.save()
            self.assertIsNotNone(car.owner.user.id)
            self.assertIsNotNone(car.owner.pk)
            self.assertIsNotNone(car.engine.id)
            self.assertIsNotNone(car.id)
