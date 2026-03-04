from unittest import TestCase
from unittest.mock import MagicMock

from src.adapters.input import ExpenseInputAdapter
from src.adapters.output import JsonOutputAdapter
from src.application.use_cases import ExpenseUseCases
from src.domain.dtos import ArgsDto


class TestExpenseInputAdapter(TestCase):
    adapter: ExpenseInputAdapter

    def setUp(self):
        repository = JsonOutputAdapter("test.json")
        input = ExpenseUseCases(repository)
        input.create = MagicMock(return_value=1)
        self.adapter = ExpenseInputAdapter(input)

    def test_add_without_arguments(self):
        result = self.adapter.add("Ether", None)
        self.assertEqual(result, 2)

    def test_add_success(self):
        result = self.adapter.add("Ether", 128.0)
        self.assertEqual(result, 0)

    def test_main_add_success(self):
        args = ArgsDto(command="add", description="Phoenix Down", amount=512.0)
        self.adapter.add = MagicMock(return_value=0)
        result = self.adapter.main(args)
        self.assertEqual(result, 0)

    def test_main_add_unknown_command(self):
        args = ArgsDto(command="heal", description="Phoenix Down", amount=512.0)
        result = self.adapter.main(args)
        self.assertEqual(result, 1)
