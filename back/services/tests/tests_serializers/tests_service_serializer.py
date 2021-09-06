from django.test import TestCase, tag
from services.factories import ServiceFactory
from services.serializers import ServiceSerializer


class ServiceSerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'title': 'example_title',
            'cost': '120.00',
            'is_active': False,
            'description': 'desc'
        }
        self.service = ServiceFactory(**self.test_data)

    @tag('service')
    def test_serializer_fields_are_not_empty(self):
        serialized_service = ServiceSerializer(instance=self.service)
        for field in serialized_service.data.values():
            self.assertIsNotNone(field)

    @tag('service')
    def test_serializer_contains_expected_data(self):
        serialized_service = ServiceSerializer(instance=self.service)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field],
                             serialized_service.data[field])
