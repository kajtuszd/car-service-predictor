from django.test import TestCase, tag
from cars.factories import EngineFactory
from cars.serializers import EngineSerializer


class EngineSerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'capacity': '2.00',
            'horsepower': 200,
            'engine_type': 'Petrol',
        }
        self.engine = EngineFactory(**self.test_data)

    @tag('engine')
    def test_serializer_fields_are_not_empty(self):
        serialized_engine = EngineSerializer(instance=self.engine)
        for field in serialized_engine.data.values():
            self.assertIsNotNone(field)

    @tag('engine')
    def test_serializer_contains_expected_data(self):
        serialized_engine = EngineSerializer(instance=self.engine)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field], serialized_engine.data[field])
