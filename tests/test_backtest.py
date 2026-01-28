from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from aistocktrader.backtest.engine import run_backtest
from aistocktrader.strategies.base import Signal


def test_run_backtest_counts_signals() -> None:
    signals = [
        Signal(symbol="AAPL", timestamp=datetime.utcnow(), action="buy", strength=0.5),
        Signal(symbol="MSFT", timestamp=datetime.utcnow(), action="sell", strength=0.2),
    ]
    result = run_backtest(signals)
    assert result.signals_processed == 2
