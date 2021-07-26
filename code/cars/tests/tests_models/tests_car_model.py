import datetime

from django.test import tag

from cars.factories import CarFactory
from cars.models import Car, Engine, return_current_year
from django.core.exceptions import ValidationError
from django.test import TestCase
from users.models import Customer, User


class CarCreationTests(TestCase):

    def setUp(self):
        self.cars = CarFactory.build_batch(3)

    @tag('slow')
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

    def test_invalid_car_brand_not_saved(self):
        invalid_car = CarFactory()
        invalid_car.brand = "Notexist"
        with self.assertRaises(ValidationError):
            invalid_car.save()

    def test_invalid_car_model_for_brand_not_saved(self):
        invalid_car = CarFactory()
        invalid_car.model = "Notexist"
        with self.assertRaises(ValidationError):
            invalid_car.save()

    def test_car_with_not_unique_registration_not_saved(self):
        car1 = CarFactory()
        car2 = CarFactory()
        car1.registration = car2.registration
        with self.assertRaises(ValidationError):
            car1.save()

    def test_multiple_cars_with_empty_registration_saved_correctly(self):
        car1 = CarFactory(registration=None)
        car2 = CarFactory(registration=None)    
        self.assertIsNotNone(car1.id)
        self.assertIsNotNone(car2.id)


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
        self.assertFalse(
            User.objects.filter(id=self.car.owner.user.id).exists()
        )
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_delete_engine_and_car_by_cascade(self):
        self.car.engine.delete()
        self.assertTrue(Customer.objects.filter(pk=self.car.owner.pk).exists())
        self.assertFalse(Engine.objects.filter(id=self.car.engine.id).exists())
        self.assertTrue(User.objects.filter(id=self.car.owner.user.id).exists())
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())


class CarModelTests(TestCase):

    def setUp(self):
        self.car = CarFactory()

    def test_car_str_method(self):
        self.assertEquals(self.car.__str__(),
                          f'{self.car.brand} {self.car.model}')

    def test_method_returning_current_year(self):
        self.assertEquals(datetime.date.today().year, return_current_year())
