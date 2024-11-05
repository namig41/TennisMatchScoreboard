from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass
class BaseEntity(ABC):

    def __post_init__(self):
        self._validate()

    @abstractmethod
    def validate(self): ...
