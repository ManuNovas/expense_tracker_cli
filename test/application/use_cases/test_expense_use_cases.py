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
        expense_id = self.use_cases.create(description="Potions", amount=128.0)
        self.assertEqual(expense_id, 1)

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

    def test_update(self):
        expense = {
            "id": 2,
            "description": "Potion",
            "amount": 128.0,
            "created_at": "2026-03-09 21:34:00",
            "updated_at": None
        }
        self.use_cases.repository_port.get_by_id = MagicMock(return_value=expense)
        self.use_cases.repository_port.update = MagicMock(return_value=True)
        result = self.use_cases.update(2, "High Potion", 256.0)
        self.assertTrue(result)

    def test_update_not_found(self):
        self.use_cases.repository_port.get_by_id = MagicMock(return_value=None)
        result = self.use_cases.update(3, "Ether", 256.0)
        self.assertEqual(result, False)

    def test_delete_success(self):
        self.use_cases.repository_port.delete = MagicMock(return_value=True)
        result = self.use_cases.delete(1)
        self.assertTrue(result)

    def test_delete_not_found(self):
        self.use_cases.repository_port.delete = MagicMock(return_value=False)
        result = self.use_cases.delete(1)
        self.assertEqual(result, False)
