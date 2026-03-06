from src.application.ports.input import ExpenseInputPort
from src.domain.dtos import ArgsDto


class ExpenseInputAdapter:
    input_port: ExpenseInputPort

    def __init__(self, input_port: ExpenseInputPort):
        self.input_port = input_port

    def add(self, description: str | None, amount: float | None):
        if not description or not amount:
            print("You should specify a description and an amount.")
            return 2
        id = self.input_port.create(description, amount)
        print(f"Expense added successfuly (ID: {id})")
        return 0
    
    def list(self):
        expenses = self.input_port.list()
        print("# ID\tDate\t\tDescription\t\tAmount")
        for expense in expenses:
            print(f"# {expense.id}\t{expense.created_at_date_format()}\t{expense.description:<24}${expense.amount}")
        return 0

    def main(self, args: ArgsDto) -> int:
        if args.command == "add":
            response = self.add(args.description, args.amount)
        elif args.command == "list":
            response = self.list()
        else:
            print("Unknown command.")
            response = 1
        return response
