from argparse import ArgumentParser

from src.adapters.input import ExpenseInputAdapter
from src.adapters.output import JsonOutputAdapter
from src.application.use_cases import ExpenseUseCases

expenses_repository = JsonOutputAdapter("expenses.json")
use_cases = ExpenseUseCases(expenses_repository)
adapter = ExpenseInputAdapter(use_cases)
parser = ArgumentParser(description="Expense tracker cli commands")
parser.add_argument("command", type=str, help="Supports: add, list and update")
parser.add_argument("-i", "--id", type=int, help="ID of expense")
parser.add_argument("-d", "--description", type=str, help="Description of expense")
parser.add_argument("-a", "--amount", type=float, help="Amount of expense")
args = parser.parse_args()
adapter.main(args)
