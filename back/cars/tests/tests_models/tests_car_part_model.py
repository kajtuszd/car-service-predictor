import random

from cars.factories import CarPartFactory
from cars.models import EngineType
from django.core.exceptions import ValidationError
from django.test import TestCase, tag


@tag('part')
class CarPartCreationTests(TestCase):

    def setUp(self):
        self.parts = CarPartFactory.build_batch(5)

    def test_save_car_part_object(self):
        for part in self.parts:
            part.category.save()
            part.car.engine.save()
            part.car.owner.workshop.save()
            part.car.owner.save()
            part.car.save()
            part.save()
            self.assertIsNotNone(part.category.id)
            self.assertIsNotNone(part.car.engine.id)
            self.assertIsNotNone(part.car.owner.workshop.id)
            self.assertIsNotNone(part.car.owner.pk)
            self.assertIsNotNone(part.car.id)
            self.assertIsNotNone(part.id)


@tag('part')
class CarPartDeletionTests(TestCase):

    def setUp(self):
        self.part = CarPartFactory()

    def test_delete_part_object(self):
        self.part.delete()
        self.assertIsNone(self.part.id)
        self.assertIsNotNone(self.part.category.id)
        self.assertIsNotNone(self.part.car.id)


@tag('part')
class CarPartModelTests(TestCase):

    def setUp(self):
        self.parts = CarPartFactory.create_batch(6)

    def test_car_part_str_method(self):
        for part in self.parts:
            self.assertEquals(part.__str__(), f'{part.category}')

    def test_car_part_chosen_drive_type_same_as_engine_type(self):
        for part in self.parts:
            if part.category.drive_type != '':
                self.assertEquals(part.category.drive_type,
                                  part.car.engine.engine_type)

    def test_car_part_chosen_drive_type_different_than_engine_type(self):
        for part in self.parts:
            if part.category.drive_type != '':
                choices = [i[0] for i in EngineType.TYPES]
                choices.remove(str(part.category.drive_type))
                part.car.engine.engine_type = random.choice(choices)
                with self.assertRaises(ValidationError, msg='Invalid car drive'
                                                            'or car part type'):
                    part.save()
