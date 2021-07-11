from django.db import IntegrityError
from django.test import TestCase
from users.factories import UserFactory


class UserModelTests(TestCase):

    def setUp(self):
        self.users = UserFactory.build_batch(3)

    def test_users_are_created_correctly(self):
        for user in self.users:
            user.save()
            self.assertIsNotNone(user.id)

    def test_creating_accounts_not_possible_with_one_email_address(self):
        self.users[1].email = self.users[0].email
        self.users[0].save()
        with self.assertRaises(IntegrityError):
            self.users[1].save()

    def test_creating_accounts_not_possible_with_one_username(self):
        self.users[1].username = self.users[0].username
        self.users[0].save()
        with self.assertRaises(IntegrityError):
            self.users[1].save()

    def test_str_method(self):
        for user in self.users:
            self.assertEquals(user.__str__(),
                              f'{user.first_name} {user.last_name}')
