from django.test import TestCase
from cars.factories import EngineFactory


class EngineCreationTests(TestCase):

    def setUp(self):
        self.engines = EngineFactory.build_batch(3)

    def test_save_engine_object(self):
        for engine in self.engines:
            engine.save()
            self.assertIsNotNone(engine.id)


class EngineDeletionTests(TestCase):

    def setUp(self):
        self.engine = EngineFactory()

    def test_save_engine_object(self):
        self.engine.delete()
        self.assertIsNone(self.engine.id)


class EngineModelTests(TestCase):

    def setUp(self):
        self.engines = EngineFactory.create_batch(3)

    def test_engine_str_method(self):
        for e in self.engines:
            self.assertEquals(e.__str__(),
                            f'{e.engine_type} {e.horsepower}HP {e.capacity}')
