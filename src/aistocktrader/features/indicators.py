"""Feature engineering helpers."""

from collections.abc import Iterable


def simple_moving_average(series: Iterable[float], window: int) -> list[float | None]:
    """Compute a simple moving average."""

    values = list(series)
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(values):
        return [None] * len(values)
    averages: list[float | None] = []
    for index in range(len(values)):
        if index + 1 < window:
            averages.append(None)
        else:
            window_slice = values[index + 1 - window : index + 1]
            averages.append(sum(window_slice) / window)
    return averages


def exponential_moving_average(series: Iterable[float], span: int) -> list[float]:
    """Compute an exponential moving average."""

    values = list(series)
    if span <= 0:
        raise ValueError("span must be positive")
    alpha = 2 / (span + 1)
    ema_values: list[float] = []
    for value in values:
        if not ema_values:
            ema_values.append(value)
        else:
            ema_values.append(alpha * value + (1 - alpha) * ema_values[-1])
    return ema_values
