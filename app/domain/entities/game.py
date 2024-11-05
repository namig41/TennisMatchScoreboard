from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.entities.player import Player
from domain.interfaces.infrastructure.logger import ILogger


@dataclass
class Game(BaseEntity):
    player_one: Player
    player_two: Player
    _logger: ILogger
