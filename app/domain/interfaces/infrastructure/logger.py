from typing import Protocol


class ILogger(Protocol):

    def info(self, message: str) -> None: ...

    def error(self, message: str) -> None: ...

    def debug(self, message: str) -> None: ...
