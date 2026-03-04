from datetime import datetime

from src.domain.entities import Expense
from src.application.ports.output import RepositoryOutputPort


class ExpenseUseCases:
    repository_port: RepositoryOutputPort

    def __init__(self, repository_port: RepositoryOutputPort):
        self.repository_port = repository_port

    def create(self, description: str, amount: float) -> int:
        expense = Expense(
            id=None,
            description=description,
            amount=amount,
            created_at=datetime.now(),
            updated_at=None
        )
        return self.repository_port.create(expense.to_dict())
