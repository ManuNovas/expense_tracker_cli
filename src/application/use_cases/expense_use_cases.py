from datetime import datetime

from src.domain.entities import Expense
from src.application.ports.input import ExpenseInputPort


class ExpenseUseCases(ExpenseInputPort):
    def create(self, description: str, amount: float) -> int:
        expense = Expense(
            expense_id=None,
            description=description,
            amount=amount,
            created_at=datetime.now(),
            updated_at=None
        )
        return self.repository_port.create(expense.to_dict())
