class Budget:
    id: int | None
    amount: float

    def __init__(self, budget_id: int | None, amount: float):
        self.id = budget_id
        self.amount = amount
