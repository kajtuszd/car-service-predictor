from django.test import TestCase, tag
from cars.factories import CarPartCategoryFactory
from cars.serializers import CarPartCategorySerializer


class CarPartCategorySerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'name': 'wheel',
            'drive_type': 'Hybrid',
        }
        self.category = CarPartCategoryFactory(**self.test_data)

    @tag('part_category')
    def test_serializer_fields_are_not_empty(self):
        serialized_category = CarPartCategorySerializer(instance=self.category)
        for field in serialized_category.data.values():
            self.assertIsNotNone(field)

    @tag('part_category')
    def test_serializer_contains_expected_data(self):
        serialized_category = CarPartCategorySerializer(instance=self.category)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field], serialized_category.data[field])
