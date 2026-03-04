from abc import ABC, abstractmethod

from src.application.ports.output import RepositoryOutputPort


class ExpenseInputPort(ABC):
    repository_port: RepositoryOutputPort

    def __init__(self, repository_port: RepositoryOutputPort):
        self.repository_port = repository_port

    @abstractmethod
    def create(self, description: str, amount: float) -> int:
        pass
