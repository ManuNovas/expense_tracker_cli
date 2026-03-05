from unittest import TestCase
from unittest.mock import MagicMock

from src.adapters.output import JsonOutputAdapter
from src.application.use_cases import ExpenseUseCases


class TestExpenseUseCases(TestCase):
    use_cases: ExpenseUseCases

    def setUp(self):
        repository_adapter = JsonOutputAdapter("expenses.json")
        self.use_cases = ExpenseUseCases(repository_adapter)

    def test_create_expense(self):
        self.use_cases.repository_port.create = MagicMock(return_value=1)
        id = self.use_cases.create(description="Potions", amount=128.0)
        self.assertEqual(id, 1)

    def test_list(self):
        items = [{
            "id": 1,
            "description": "Potion",
            "amount": 64,
            "created_at": "2026-02-04T00:00:00",
            "updated_at": "2026-02-05T00:00:00"
        }]
        self.use_cases.repository_port.get_all = MagicMock(return_value=items)
        expenses = self.use_cases.list()
        self.assertEqual(items[0]["id"], expenses[0].id)
        self.assertEqual(items[0]["description"], expenses[0].description)
        self.assertEqual(items[0]["amount"], expenses[0].amount)
        self.assertEqual(items[0]["created_at"], expenses[0].created_at.isoformat())
        self.assertEqual(items[0]["updated_at"], expenses[0].updated_at.isoformat())
