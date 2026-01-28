"""ML training entry points."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingReport:
    model_name: str
    trained_samples: int


def train_model(samples: int, model_name: str = "baseline") -> TrainingReport:
    """Placeholder training routine."""

    return TrainingReport(model_name=model_name, trained_samples=samples)
