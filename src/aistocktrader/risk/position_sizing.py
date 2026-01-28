"""Risk and position sizing helpers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PositionSize:
    symbol: str
    quantity: float
    confidence: float


def cap_position_size(desired: float, max_pct: float) -> float:
    """Cap position size by maximum percentage of portfolio."""

    return min(desired, max_pct)
