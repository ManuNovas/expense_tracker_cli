from datetime import datetime

from src.application.domain import Expense
from src.ports.output import RepositoryOutputPort


class ExpenseUseCases:
    repository_port: RepositoryOutputPort

    def __init__(self):
        self.repository_port = RepositoryOutputPort()

    def create(self, description: str, amount: float) -> int:
        expense = Expense(
            id=None,
            description=description,
            amount=amount,
            created_at=datetime.now(),
            updated_at=None
        )
        return self.repository_port.create_expense(expense)
