from cars.factories import CarPartFactory
from django.test import TestCase, tag


@tag('part')
class CarPartCreationTests(TestCase):

    def setUp(self):
        self.parts = CarPartFactory.build_batch(3)

    def test_save_car_part_object(self):
        for part in self.parts:
            part.category.save()
            part.save()
            self.assertIsNotNone(part.id)
            self.assertIsNotNone(part.category.id)


@tag('part')
class CarPartDeletionTests(TestCase):

    def setUp(self):
        self.part = CarPartFactory()

    def test_delete_part_object(self):
        self.part.delete()
        self.assertIsNone(self.part.id)
        self.assertIsNotNone(self.part.category.id)


@tag('part')
class CarPartModelTests(TestCase):

    def setUp(self):
        self.parts = CarPartFactory.create_batch(3)

    def test_car_part_str_method(self):
        for part in self.parts:
            self.assertEquals(part.__str__(), f'{part.category}')
