from src.adapters.output import JsonOutputAdapter
from src.application.domain import Expense


class RepositoryOutputPort:
    expense_adapter: JsonOutputAdapter

    def __init__(self):
        self.expense_adapter = JsonOutputAdapter("expenses.json")

    def create_expense(self, expense: Expense) -> int:
        return self.expense_adapter.create(expense.__dict__)
