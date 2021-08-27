from cars.factories import EngineFactory
from django.test import TestCase, tag


@tag('engine')
class EngineCreationTests(TestCase):

    def setUp(self):
        self.engines = EngineFactory.build_batch(3)

    def test_save_engine_object(self):
        for engine in self.engines:
            engine.save()
            self.assertIsNotNone(engine.id)


@tag('engine')
class EngineDeletionTests(TestCase):

    def setUp(self):
        self.engine = EngineFactory()

    def test_delete_engine_object(self):
        self.engine.delete()
        self.assertIsNone(self.engine.id)


@tag('engine')
class EngineModelTests(TestCase):

    def setUp(self):
        self.engines = EngineFactory.create_batch(3)

    def test_engine_str_method(self):
        for e in self.engines:
            self.assertEquals(e.__str__(),
                              f'{e.engine_type} {e.horsepower}HP {e.capacity}')
