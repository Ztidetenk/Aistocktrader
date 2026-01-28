"""Strategy interfaces."""

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


@dataclass(frozen=True)
class Signal:
    symbol: str
    timestamp: datetime
    action: str
    strength: float


class Strategy(Protocol):
    """Strategy protocol for generating signals."""

    def generate_signals(self) -> list[Signal]:
        ...
