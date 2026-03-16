from src.domain.enums import Command


class ArgsDto:
    command: Command
    description: str | None
    amount: float | None
    id: int | None
    month: int | None

    def __init__(self, command: Command, description: str | None = None, amount: float | None = None,
                 expense_id: int | None = None, month: int | None = None):
        self.command = command
        self.description = description
        self.amount = amount
        self.id = expense_id
        self.month = month
