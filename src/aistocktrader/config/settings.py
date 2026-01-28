"""Configuration settings for Aistocktrader."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DataSettings:
    """Settings for data ingestion and storage."""

    timezone: str = "UTC"
    market_hours: str = "09:30-16:00"


@dataclass(frozen=True)
class RiskSettings:
    """Default risk limits."""

    max_position_pct: float = 0.1
    daily_loss_limit_pct: float = 0.02


@dataclass(frozen=True)
class Settings:
    """Aggregate settings."""

    data: DataSettings = DataSettings()
    risk: RiskSettings = RiskSettings()


DEFAULT_SETTINGS = Settings()
