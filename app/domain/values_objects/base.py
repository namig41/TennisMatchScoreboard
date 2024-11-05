from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)


VT = TypeVar("VT")


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self._validate()

    @abstractmethod
    def validate(self): ...

    @abstractmethod
    def as_type_value(self) -> VT: ...
