from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from src.application.domain import Expense
from src.ports.output import RepositoryOutputPort


class TestRepositoryOutputPort(TestCase):
    port: RepositoryOutputPort

    def setUp(self):
        self.port = RepositoryOutputPort()

    def test_create_expense(self):
        self.port.expense_adapter.create = MagicMock(return_value=1)
        id = self.port.create_expense(Expense(
            id=None,
            description="Potions",
            amount=128.0,
            created_at=datetime.now().isoformat(),
            updated_at=None
        ))
        self.assertEqual(id, 1)