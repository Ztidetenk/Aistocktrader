from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from aistocktrader.features.indicators import simple_moving_average


def test_simple_moving_average() -> None:
    series = [1, 2, 3, 4]
    result = simple_moving_average(series, window=2)
    assert result == [None, 1.5, 2.5, 3.5]
