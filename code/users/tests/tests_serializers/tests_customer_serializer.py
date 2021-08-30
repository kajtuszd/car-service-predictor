from django.test import TestCase, tag
from users.factories import CustomerFactory
from users.serializers import CustomerSerializer


class CustomerSerializerTests(TestCase):

    def setUp(self):
        self.customer = CustomerFactory()

    @tag('customer')
    def test_serializer_fields_are_not_empty(self):
        serialized_customer = CustomerSerializer(instance=self.customer)
        for field in serialized_customer.data.values():
            self.assertIsNotNone(field)
