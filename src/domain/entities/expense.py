from datetime import datetime

class Expense:
    id: int | None
    description: str
    amount: float
    created_at: datetime
    updated_at: datetime

    def __init__(self, id: int | None, description: str, amount: str, created_at: datetime, updated_at = datetime | None):
        self.id = id
        self.description = description
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at
