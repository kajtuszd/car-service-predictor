from django.test import TestCase, tag
from users.factories import UserFactory
from users.serializers import UserSerializer


class UserSerializerTests(TestCase):

    def setUp(self):
        self.test_data = {
            'first_name': 'exampleName',
            'last_name': 'exampleSurname',
            'email': 'example@ex.com',
            'city': 'London'
        }
        self.user = UserFactory(**self.test_data)

    @tag('user')
    def test_serializer_contains_expected_data(self):
        serialized_user = UserSerializer(instance=self.user)
        for field in self.test_data.keys():
            self.assertEqual(self.test_data[field], serialized_user.data[field])
