from unittest import TestCase
from unittest.mock import patch, mock_open, MagicMock

from src.adapters.output import JsonOutputAdapter


class TestJsonOutputAdapter(TestCase):
    adapter: JsonOutputAdapter

    def setUp(self):
        self.adapter = JsonOutputAdapter("users_test.json")

    @patch("src.adapters.output.json_output_adapter.exists")
    def test_open_new(self, exists_mock):
        exists_mock.return_value = False
        with patch("builtins.open", mock_open()) as write_file:
            with patch("builtins.open", mock_open(read_data="[]")) as read_file:
                self.adapter.open()
                self.assertEqual(self.adapter.data, [])
                read_file.assert_called_with("users_test.json", "r")

    @patch("src.adapters.output.json_output_adapter.exists")
    def test_open_existing(self, exists_mock):
        exists_mock.return_value = True
        with patch("builtins.open", mock_open(read_data='[{"id": 1}]')) as read_file:
            self.adapter.open()
            self.assertEqual(self.adapter.data, [{"id": 1}])
            read_file.assert_called_with("users_test.json", "r")

    def test_get_next_id(self):
        self.adapter.data = [{"id": 1}]
        next_id = self.adapter.get_next_id()
        self.assertEqual(next_id, 2)

    def test_save(self):
        with patch("builtins.open", mock_open()) as write_file:
            self.adapter.data = [{"id": 1}]
            self.adapter.save()
            write_file.assert_called_with("users_test.json", "w")

    def test_create(self):
        item = {
            "name": "Clive Rosfield",
            "email": "clive@rosfield.test"
        }
        self.adapter.open = MagicMock()
        self.adapter.get_next_id = MagicMock(return_value=1)
        self.adapter.save = MagicMock()
        created_id = self.adapter.create(item)
        self.assertEqual(created_id, 1)

    def test_get_all(self):
        items = [
            {
                "id": 1,
                "name": "Clive Rosfield",
                "email": "clive@rosfield.test"
            }
        ]
        self.adapter.open = MagicMock()
        self.adapter.data = items
        data = self.adapter.get_all()
        self.assertEqual(items, data)

    def test_get_by_id(self):
        items = [
            {
                "id": 1,
                "name": "Clive Rosfield",
                "email": "clive@rosfield.test"
            }
        ]
        self.adapter.open = MagicMock()
        self.adapter.data = items
        result = self.adapter.get_by_id(1)
        self.assertEqual(items[0], result)

    def test_get_by_id_not_found(self):
        items = [
            {
                "id": 1,
                "name": "Clive Rosfield",
                "email": "clive@rosfield.test"
            }
        ]
        self.adapter.open = MagicMock()
        self.adapter.data = items
        result = self.adapter.get_by_id(2)
        self.assertEqual(None, result)

    def test_update(self):
        self.adapter.open = MagicMock()
        self.adapter.data = [
            {
                "id": 1,
                "name": "Clive Rosfield",
                "email": "clive@rosfield.test"
            },
            {
                "id": 2,
                "name": "Clive Rosfield",
                "email": "clive@rosfield.test"
            }
        ]
        self.adapter.save = MagicMock()
        item = {
            "id": 2,
            "name": "Joshua Rosfield",
            "email": "joshua@rosfield.test"
        }
        updated = self.adapter.update(item)
        self.assertTrue(updated)
        self.assertEqual(self.adapter.data[1], item)

    def test_delete(self):
        self.adapter.open = MagicMock()
        self.adapter.data = [
            {
                "id": 1,
                "name": "Clive Rosfield",
                "email": "clive@rosfield.test"
            },
            {
                "id": 2,
                "name": "Joshua Rosfield",
                "email": "joshua@rosfield.test"
            }
        ]
        self.adapter.save = MagicMock()
        self.adapter.delete(2)
        self.assertTrue(len(self.adapter.data) == 1)
        self.assertEqual(self.adapter.data[0]["id"], 1)
