from abc import ABC, abstractmethod
from model_data.model import Entity
from typing import List


class Repository(ABC):

    @abstractmethod
    def select(self, params: tuple) -> List[Entity]:
        pass

    @abstractmethod
    def insert(self, entities: List[Entity]) -> int:
        pass
