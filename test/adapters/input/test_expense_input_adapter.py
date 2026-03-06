from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from src.adapters.input import ExpenseInputAdapter
from src.adapters.output import JsonOutputAdapter
from src.application.use_cases import ExpenseUseCases
from src.domain.dtos import ArgsDto
from src.domain.entities import Expense


class TestExpenseInputAdapter(TestCase):
    adapter: ExpenseInputAdapter

    def setUp(self):
        repository = JsonOutputAdapter("expenses.json")
        input = ExpenseUseCases(repository)
        input.create = MagicMock(return_value=1)
        self.adapter = ExpenseInputAdapter(input)

    def test_add_without_arguments(self):
        result = self.adapter.add("Ether", None)
        self.assertEqual(result, 2)

    def test_add_success(self):
        result = self.adapter.add("Ether", 128.0)
        self.assertEqual(result, 0)

    def test_list(self):
        expenses = [
            Expense(
                expense_id=1,
                description="Potion",
                amount=64,
                created_at=datetime.now(),
                updated_at=None,
            ),
            Expense(
                expense_id=1,
                description="Ether",
                amount=128,
                created_at=datetime.now(),
                updated_at=None,
            ),
        ]
        self.adapter.input_port.list = MagicMock(return_value=expenses)
        result = self.adapter.list()
        self.assertEqual(result, 0)

    def test_main_add_success(self):
        args = ArgsDto(command="add", description="Phoenix Down", amount=512.0)
        self.adapter.add = MagicMock(return_value=0)
        result = self.adapter.main(args)
        self.assertEqual(result, 0)

    def test_main_list(self):
        args = ArgsDto(command="list", description=None, amount=None)
        self.adapter.list = MagicMock(return_value=0)
        result = self.adapter.main(args)
        self.assertEqual(result, 0)

    def test_main_add_unknown_command(self):
        args = ArgsDto(command="heal", description="Phoenix Down", amount=512.0)
        result = self.adapter.main(args)
        self.assertEqual(result, 1)
