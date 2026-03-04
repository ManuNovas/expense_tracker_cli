class ArgsDto:
    command: str
    description: str | None
    amount: float | None

    def __init__(self, command: str, description: str | None, amount: float | None):
        self.command = command
        self.description = description
        self.amount = amount
