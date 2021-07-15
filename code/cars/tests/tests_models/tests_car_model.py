from django.test import TestCase
from cars.factories import CarFactory
from users.models import User, Customer
from cars.models import Car, Engine


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


class CarDeletionTests(TestCase):

    def setUp(self):
        self.car = CarFactory()

    def test_delete_car_and_not_delete_other_car_objects(self):
        self.car.delete()
        self.assertTrue(Customer.objects.filter(pk=self.car.owner.pk).exists())
        self.assertTrue(Engine.objects.filter(id=self.car.engine.id).exists())
        self.assertTrue(User.objects.filter(id=self.car.owner.user.id).exists())
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_delete_owner_and_car_by_cascade(self):
        user = self.car.owner.user
        self.car.owner.delete()
        self.assertFalse(Customer.objects.filter(pk=self.car.owner.pk).exists())
        self.assertTrue(Engine.objects.filter(id=self.car.engine.id).exists())
        self.assertTrue(User.objects.filter(id=user.id).exists())
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_delete_user_and_owner_with_car_by_cascade(self):
        self.car.owner.user.delete()
        self.assertFalse(Customer.objects.filter(pk=self.car.owner.pk).exists())
        self.assertTrue(Engine.objects.filter(id=self.car.engine.id).exists())
        self.assertFalse(User.objects.filter(id=self.car.owner.user.id).exists())
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_delete_engine_and_car_by_cascade(self):
        self.car.engine.delete()
        self.assertTrue(Customer.objects.filter(pk=self.car.owner.pk).exists())
        self.assertFalse(Engine.objects.filter(id=self.car.engine.id).exists())
        self.assertTrue(User.objects.filter(id=self.car.owner.user.id).exists())
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())
