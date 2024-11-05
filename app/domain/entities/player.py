from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.interfaces.infrastructure.logger import ILogger


@dataclass
class Player(BaseEntity):
    name: str
    _logger: ILogger
