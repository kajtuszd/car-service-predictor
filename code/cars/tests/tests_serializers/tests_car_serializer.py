from django.test import TestCase, tag
from cars.factories import CarFactory
from cars.serializers import CarSerializer


class CarSerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'brand': 'Toyota',
            'model': 'Corolla',
            'production_year': 2000,
        }
        self.car = CarFactory(**self.test_data)

    @tag('car')
    def test_serializer_fields_are_not_empty(self):
        serialized_category = CarSerializer(instance=self.car)
        for field in serialized_category.data.values():
            self.assertIsNotNone(field)

    @tag('car')
    def test_serializer_contains_expected_data(self):
        serialized_category = CarSerializer(instance=self.car)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field], serialized_category.data[field])
