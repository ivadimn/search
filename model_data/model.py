from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List


@dataclass
class Entity(ABC):
    id: int
    name: str

    @abstractmethod
    def display(self, locale: str) -> str:
        pass


@dataclass
class User(Entity):
    locale: str



    def display(self, locale: str) -> str:
        pass

    def clear_data(self):
        self.data.clear()
        self.params.clear()


@dataclass
class Food(Entity):
    group_id: int
    kkal: float
    belki: float
    fats: float
    ugl: float
    url: str


    def display(self, locale: str) -> str:
        return "{0}\n{1}: {2}{3}\n{4}: {5}\n{6}: {7}\n{8}: {9}".format(
            self.name, "Энергетическая ценность", "кКал.",
            self.kkal, "Белки", self.belki,
            "Жиры", self.fats,
            "Углеводы", self.ugl
        )

    def __str__(self):
        return self.display("ru_RU")


@dataclass
class FoodGroup(Entity):
    url: str

    def display(self, locale: str) -> str:
        return "{0}: {1}".format(self.name, self.url)


@dataclass
class Mat:
    id: int
    word: str