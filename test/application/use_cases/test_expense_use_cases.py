from unittest import TestCase
from unittest.mock import MagicMock

from src.application.use_cases import ExpenseUseCases


class TestExpenseUseCases(TestCase):
    use_cases: ExpenseUseCases

    def setUp(self):
        self.use_cases = ExpenseUseCases()

    def test_create_expense(self):
        self.use_cases.repository_port.create_expense = MagicMock(return_value=1)
        id = self.use_cases.create(description="Potions", amount=128.0)
        self.assertEqual(id, 1)
