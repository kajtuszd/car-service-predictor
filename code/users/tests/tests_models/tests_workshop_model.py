from django.test import TestCase, tag
from users.factories import WorkshopFactory
from users.models import User, Workshop


@tag('workshop')
class WorkshopCreationTests(TestCase):

    def setUp(self):
        self.workshop = WorkshopFactory()

    def test_workshops_are_created_correctly(self):
        self.assertIsNotNone(self.workshop.user.id)
        self.assertIsNotNone(self.workshop.pk)

    def test_workshop_is_deleted_and_user_not_deleted(self):
        user = User.objects.get(id=self.workshop.user.id)
        self.workshop.delete()
        self.assertIsNotNone(user.id)
        self.assertFalse(Workshop.objects.filter(pk=self.workshop.pk).exists())

    def test_user_deleted_and_workshop_deleted_by_cascade(self):
        user = User.objects.get(id=self.workshop.user.id)
        user.delete()
        self.assertIsNone(user.id)
        self.assertFalse(Workshop.objects.filter(pk=self.workshop.pk).exists())


@tag('workshop')
class WorkshopModelTests(TestCase):

    def setUp(self):
        self.workshops = WorkshopFactory.create_batch(3)

    def test_str_method(self):
        for workshop in self.workshops:
            self.assertEquals(workshop.__str__(), f'{workshop.workshop_name}')
