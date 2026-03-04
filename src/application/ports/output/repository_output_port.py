from abc import ABC, abstractmethod


class RepositoryOutputPort(ABC):
    @abstractmethod
    def create(self, item: dict) -> int:
        pass

    @abstractmethod
    def get_all() -> list[dict]:
        pass

    @abstractmethod
    def update(self, item: dict) -> bool:
        pass
