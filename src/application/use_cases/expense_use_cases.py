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
    
    def list(self) -> list[Expense]:
        expenses = []
        items = self.repository_port.get_all()
        for item in items:
            expense = Expense(
                expense_id=item["id"],
                description=item["description"],
                amount=item["amount"],
                created_at=datetime.fromisoformat(item["created_at"]),
                updated_at=datetime.fromisoformat(item["updated_at"]) if item["updated_at"] is not None else None
            )
            expenses.append(expense)
        return expenses
    
    def update(self, expense_id: int, description: str | None, amount: float | None) -> bool:
        expense = self.repository_port.get_by_id(expense_id)
        if expense is None:
            return False
        if description is not None:
            expense["description"] = description
        if amount is not None:
            expense["amount"] = amount
        expense["updated_at"] = datetime.now().isoformat()
        return self.repository_port.update(expense)

    def delete(self, expense_id: int) -> bool:
        return self.repository_port.delete(expense_id)
