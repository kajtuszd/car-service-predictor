from django.test import TestCase
from users.factories import WorkshopFactory


class WorkshopModelTests(TestCase):

    def setUp(self):
        self.workshops = WorkshopFactory.build_batch(3)

    def test_workshops_are_created_correctly(self):
        for workshop in self.workshops:
            workshop.user.save()
            workshop.save()
            self.assertIsNotNone(workshop.user.id)
            self.assertIsNotNone(workshop.pk)
