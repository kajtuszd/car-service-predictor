from django.test import TestCase
from users.factories import CustomerFactory
from users.models import Customer, User


class CustomerCreationTests(TestCase):

    def setUp(self):
        self.customer = CustomerFactory()

    def test_customers_are_created_correctly(self):
        self.assertIsNotNone(self.customer.user.id)
        self.assertIsNotNone(self.customer.pk)

    def test_customer_is_deleted_and_user_not_deleted(self):
        user = User.objects.get(id=self.customer.user.id)
        self.customer.delete()
        self.assertIsNotNone(user.id)
        self.assertFalse(Customer.objects.filter(pk=self.customer.pk).exists())

    def test_user_deleted_and_customer_deleted_by_cascade(self):
        user = User.objects.get(id=self.customer.user.id)
        user.delete()
        self.assertIsNone(user.id)
        self.assertFalse(Customer.objects.filter(pk=self.customer.pk).exists())


class CustomerModelTests(TestCase):

    def setUp(self):
        self.customers = CustomerFactory.create_batch(3)

    def test_str_method(self):
        for customer in self.customers:
            self.assertEquals(customer.__str__(), 
                    f'{customer.user.first_name} {customer.user.last_name}')
