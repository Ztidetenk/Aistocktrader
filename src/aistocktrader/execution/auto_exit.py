"""Auto-exit helpers for stop-loss and take-profit."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExitSignal:
    symbol: str
    action: str
    reason: str


def evaluate_exit(
    symbol: str,
    entry_price: float,
    current_price: float,
    stop_loss_pct: float,
    take_profit_pct: float,
) -> ExitSignal | None:
    """Return an exit signal when stop-loss or take-profit is triggered."""

    if stop_loss_pct <= 0 or take_profit_pct <= 0:
        raise ValueError("stop_loss_pct and take_profit_pct must be positive")
    if entry_price <= 0:
        raise ValueError("entry_price must be positive")

    stop_price = entry_price * (1 - stop_loss_pct)
    take_profit_price = entry_price * (1 + take_profit_pct)

    if current_price <= stop_price:
        return ExitSignal(symbol=symbol, action="sell", reason="stop_loss")
    if current_price >= take_profit_price:
        return ExitSignal(symbol=symbol, action="sell", reason="take_profit")
    return None
