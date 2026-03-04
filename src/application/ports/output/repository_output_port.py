from abc import ABC, abstractmethod


class RepositoryOutputPort(ABC):
    @abstractmethod
    def create(self, item: dict) -> int:
        pass
