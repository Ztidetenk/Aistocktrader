"""Order management system scaffolding."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Order:
    symbol: str
    side: str
    quantity: float
    timestamp: datetime
    reason: str | None = None


def submit_order(order: Order) -> Order:
    """Submit an order to the broker adapter (placeholder)."""

    return order
