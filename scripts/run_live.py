"""Run a minimal live/paper trading loop (scaffold)."""

from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from aistocktrader.execution.auto_exit import evaluate_exit
from aistocktrader.execution.oms import Order, submit_order
from aistocktrader.strategies.base import Signal


def main() -> None:
    signal = Signal(
        symbol="AAPL",
        timestamp=datetime.utcnow(),
        action="buy",
        strength=0.6,
    )
    order = Order(
        symbol=signal.symbol,
        side=signal.action,
        quantity=1.0,
        timestamp=datetime.utcnow(),
        reason="entry",
    )
    submitted = submit_order(order)
    print(f"Submitted order: {submitted}")

    exit_signal = evaluate_exit(
        symbol=signal.symbol,
        entry_price=100.0,
        current_price=106.0,
        stop_loss_pct=0.02,
        take_profit_pct=0.05,
    )
    if exit_signal:
        exit_order = Order(
            symbol=exit_signal.symbol,
            side=exit_signal.action,
            quantity=1.0,
            timestamp=datetime.utcnow(),
            reason=exit_signal.reason,
        )
        submitted_exit = submit_order(exit_order)
        print(f"Submitted exit order: {submitted_exit}")


if __name__ == "__main__":
    main()
