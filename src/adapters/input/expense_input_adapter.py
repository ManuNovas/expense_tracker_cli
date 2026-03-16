from calendar import month_name

from src.application.ports.input import ExpenseInputPort
from src.domain.dtos import ArgsDto
from src.domain.enums import Command


class ExpenseInputAdapter:
    input_port: ExpenseInputPort

    def __init__(self, input_port: ExpenseInputPort):
        self.input_port = input_port

    def add(self, description: str | None, amount: float | None):
        if not description or not amount:
            print("You should specify a description and an amount.")
            return 2
        if amount < 0:
            print("The amount must be positive.")
            return 5
        expense_id = self.input_port.create(description, amount)
        print(f"Expense added successfully (ID: {expense_id})")
        return 0
    
    def list(self):
        expenses = self.input_port.list()
        print("# ID\tDate\t\tDescription\t\tAmount")
        for expense in expenses:
            print(f"# {expense.id}\t{expense.created_at_date_format()}\t{expense.description:<24}${expense.amount}")
        return 0

    def update(self, expense_id: int, description: str | None, amount: float | None):
        if amount is not None and amount < 0:
            print("The amount must be positive.")
            return 5
        updated = self.input_port.update(expense_id, description, amount)
        if not updated:
            print("The expense is not found")
            return 3
        print(f"Expense updated successfully (ID: {expense_id})")
        return 0

    def delete(self, expense_id: int):
        deleted = self.input_port.delete(expense_id)
        if not deleted:
            print("The expense is not found")
            return 3
        print(f"Expense deleted successfully (ID: {expense_id})")
        return 0

    def summary(self, month: int | None):
        if month is not None and (month < 1 or month > 12):
            print("The month must be between 1 and 12")
            return 4
        summary = self.input_port.summary(month)
        month_description = f" for {month_name[month]}" if month is not None else ""
        print(f"Total expenses{month_description}: ${summary}")
        return 0

    def main(self, args: ArgsDto) -> int:
        if args.command == Command.ADD:
            response = self.add(args.description, args.amount)
        elif args.command == Command.LIST:
            response = self.list()
        elif args.command == Command.UPDATE:
            response = self.update(args.id, args.description, args.amount)
        elif args.command == Command.DELETE:
            response = self.delete(args.id)
        elif args.command == Command.SUMMARY:
            response = self.summary(args.month)
        else:
            print("Unknown command.")
            response = 1
        return response
