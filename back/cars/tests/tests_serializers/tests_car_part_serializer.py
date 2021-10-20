from django.test import TestCase, tag
from cars.factories import CarPartFactory
from cars.serializers import CarPartSerializer


class CarPartSerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'description': 'desc',
        }
        self.car_part = CarPartFactory(**self.test_data)

    @tag('part')
    def test_serializer_contains_expected_data(self):
        serialized_category = CarPartSerializer(instance=self.car_part)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field], serialized_category.data[field])
