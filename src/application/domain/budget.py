class Budget:
    id: int | None
    amount: float

    def __init__(self, id: int | None, amount: float):
        self.id = id
        self.amount = amount
