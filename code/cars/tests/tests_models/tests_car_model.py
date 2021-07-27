import datetime

from cars.factories import CarFactory, CarPartFactory
from cars.models import Car, CarPart, Engine, return_current_year
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from users.models import Customer, User


@tag('car')
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


@tag('car')
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


@tag('car')
class CarModelTests(TestCase):

    def setUp(self):
        self.car = CarFactory()

    def test_car_str_method(self):
        self.assertEquals(self.car.__str__(),
                          f'{self.car.brand} {self.car.model}')

    def test_method_returning_current_year(self):
        self.assertEquals(datetime.date.today().year, return_current_year())


@tag('car')
class CarPartsTests(TestCase):

    def setUp(self):
        self.car = CarFactory.create(
            parts=tuple(CarPartFactory.create_batch(5)))

    def test_car_parts_generation(self):
        self.assertIsNotNone(self.car.id)
        for part in self.car.parts.all():
            self.assertIsNotNone(part.id)

    def test_car_parts_deletion(self):
        for part in self.car.parts.all():
            part.delete()
            self.assertFalse(CarPart.objects.filter(id=part.id).exists())
        self.assertIsNotNone(self.car.id)

    def test_car_deletion(self):
        parts = self.car.parts.all()
        self.car.delete()
        for part in parts:
            self.assertTrue(CarPart.objects.filter(id=part.id).exists())
        self.assertIsNone(self.car.id)

    def test_car_part_chosen_drive_type_same_as_engine_type(self):
        for part in self.car.parts.all():
            if part.category.drive_type != '':
                self.assertEquals(part.category.drive_type,
                                  self.car.engine.engine_type)
