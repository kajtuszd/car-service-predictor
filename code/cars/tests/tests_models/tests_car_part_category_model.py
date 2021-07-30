from cars.factories import CarPartCategoryFactory
from django.db.utils import IntegrityError
from django.test import TestCase, tag


@tag('part_category')
class CarPartCategoryCreationTests(TestCase):

    def setUp(self):
        self.categories = CarPartCategoryFactory.build_batch(5)

    def test_categories_creation(self):
        for category in self.categories:
            category.save()
            self.assertIsNotNone(category.id)


@tag('part_category')
class CategoryDeletionTests(TestCase):

    def setUp(self):
        self.category = CarPartCategoryFactory()

    def test_delete_category_object(self):
        self.category.delete()
        self.assertIsNone(self.category.id)


@tag('part_category')
class CategoryModelTests(TestCase):

    def test_category_str_method(self):
        categories = CarPartCategoryFactory.create_batch(3)
        for category in categories:
            if category.drive_type == '':
                self.assertEquals(category.__str__(), f'{category.name}')
            else:
                self.assertEquals(category.__str__(),
                                  f'{category.name} ({category.drive_type})')

    def test_unique_car_part_category_constraint(self):
        category1 = CarPartCategoryFactory()
        with self.assertRaises(IntegrityError,
                               msg="duplicate key value violates unique "
                                   "constraint 'unique_part_category'"):
            category2 = CarPartCategoryFactory(name=category1.name,
                                               drive_type=category1.drive_type)
