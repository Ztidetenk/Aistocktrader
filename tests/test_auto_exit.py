from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from aistocktrader.execution.auto_exit import evaluate_exit


def test_evaluate_exit_stop_loss() -> None:
    signal = evaluate_exit(
        symbol="AAPL",
        entry_price=100.0,
        current_price=97.0,
        stop_loss_pct=0.02,
        take_profit_pct=0.05,
    )
    assert signal is not None
    assert signal.reason == "stop_loss"


def test_evaluate_exit_take_profit() -> None:
    signal = evaluate_exit(
        symbol="AAPL",
        entry_price=100.0,
        current_price=106.0,
        stop_loss_pct=0.02,
        take_profit_pct=0.05,
    )
    assert signal is not None
    assert signal.reason == "take_profit"
