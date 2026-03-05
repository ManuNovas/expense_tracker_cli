from abc import ABC, abstractmethod


class RepositoryOutputPort(ABC):
    @abstractmethod
    def create(self, item: dict) -> int:
        pass

    @abstractmethod
    def get_all(self) -> list[dict]:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> dict | None:
        pass

    @abstractmethod
    def update(self, item: dict) -> bool:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        pass
