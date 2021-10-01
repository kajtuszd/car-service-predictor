from django.test import TestCase, tag
from users.factories import WorkshopFactory


@tag('workshop')
class WorkshopCreationTests(TestCase):

    def setUp(self):
        self.workshop = WorkshopFactory()

    def test_workshops_are_created_correctly(self):
        self.assertIsNotNone(self.workshop.id)


@tag('workshop')
class WorkshopModelTests(TestCase):

    def setUp(self):
        self.workshops = WorkshopFactory.create_batch(3)

    def test_str_method(self):
        for workshop in self.workshops:
            self.assertEquals(workshop.__str__(), f'{workshop.workshop_name}')
