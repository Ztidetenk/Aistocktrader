"""Market data ingestion scaffolding."""

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable


@dataclass(frozen=True)
class DataPoint:
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


def ingest_points(points: Iterable[DataPoint]) -> list[DataPoint]:
    """Ingest datapoints into the system.

    This placeholder returns the normalized list and will later persist to storage.
    """

    return list(points)
