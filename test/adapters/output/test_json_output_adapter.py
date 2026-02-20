from unittest import TestCase

from src.adapters.output import JsonOutputAdapter


class TestJsonOutputAdapter(TestCase):
    adapter: JsonOutputAdapter

    def setUp(self):
        self.adapter = JsonOutputAdapter("test.json")

    def test_create(self):
        item = {
            "name": "Clive Rosfield",
            "email": "clive@rosfield.test"
        }
        id = self.adapter.create(item)
        self.assertEqual(id > 0, True)
