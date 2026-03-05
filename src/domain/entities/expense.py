from datetime import datetime


class Expense:
    id: int | None
    description: str
    amount: float
    created_at: datetime
    updated_at: datetime | None

    def __init__(self, expense_id: int | None, description: str, amount: float, created_at: datetime,
                 updated_at=datetime | None):
        self.id = expense_id
        self.description = description
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None
        }
