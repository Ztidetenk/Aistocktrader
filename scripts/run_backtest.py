"""Run a minimal backtest to verify wiring."""

from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from aistocktrader.backtest.engine import run_backtest
from aistocktrader.strategies.base import Signal


def main() -> None:
    signals = [
        Signal(symbol="AAPL", timestamp=datetime.utcnow(), action="buy", strength=0.7),
        Signal(symbol="AAPL", timestamp=datetime.utcnow(), action="sell", strength=0.4),
    ]
    result = run_backtest(signals)
    print(f"Signals processed: {result.signals_processed}")


if __name__ == "__main__":
    main()
