from django.test import TestCase, tag
from users.factories import WorkshopFactory
from users.serializers import WorkshopSerializer


class WorkshopSerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'workshop_name': 'exampleName',
        }
        self.workshop = WorkshopFactory(**self.test_data)

    @tag('workshop')
    def test_serializer_fields_are_not_empty(self):
        serialized_workshop = WorkshopSerializer(instance=self.workshop)
        for field in serialized_workshop.data.values():
            self.assertIsNotNone(field)

    @tag('workshop')
    def test_serializer_contains_expected_data(self):
        serialized_workshop = WorkshopSerializer(instance=self.workshop)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field],
                             serialized_workshop.data[field])
