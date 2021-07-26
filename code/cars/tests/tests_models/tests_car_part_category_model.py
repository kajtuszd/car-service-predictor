from cars.factories import CarPartCategoryFactory
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

    def setUp(self):
        self.categories = CarPartCategoryFactory.create_batch(3)

    def test_category_str_method(self):
        for category in self.categories:
            if category.drive_type == '':
                self.assertEquals(category.__str__(), f'{category.name}')
            else:
                self.assertEquals(category.__str__(),
                                  f'{category.name} ({category.drive_type})')
