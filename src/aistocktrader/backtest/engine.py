"""Backtesting engine scaffolding."""

from dataclasses import dataclass
from typing import Iterable

from aistocktrader.strategies.base import Signal


@dataclass(frozen=True)
class BacktestResult:
    signals_processed: int


def run_backtest(signals: Iterable[Signal]) -> BacktestResult:
    """Run a minimal backtest by counting signals."""

    count = sum(1 for _ in signals)
    return BacktestResult(signals_processed=count)
