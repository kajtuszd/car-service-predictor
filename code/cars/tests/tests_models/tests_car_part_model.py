from cars.factories import CarPartFactory
from django.test import TestCase, tag


@tag('part')
class CarPartCreationTests(TestCase):

    def setUp(self):
        self.parts = CarPartFactory.build_batch(5)

    def test_save_car_part_object(self):
        for part in self.parts:
            part.category.save()
            part.car.engine.save()
            part.car.owner.user.save()
            part.car.owner.save()
            part.car.save()
            part.save()
            self.assertIsNotNone(part.category.id)
            self.assertIsNotNone(part.car.engine.id)
            self.assertIsNotNone(part.car.owner.user.id)
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
    