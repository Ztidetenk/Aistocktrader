# Aistocktrader

This repository scaffolds the AI trading bot described in `PLAN.md`. The initial structure focuses on
Python-based data ingestion, feature engineering, risk controls, and backtesting. As the project grows,
modules will be extended with broker integrations, ML/RL training, and monitoring tooling.

## Structure
- `src/aistocktrader/`: Core Python package.
- `scripts/`: Entry-point scripts for data pulls, backtests, and training runs.
- `tests/`: Unit tests for data validation, indicators, and strategy logic.

## Getting started
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running
```bash
python scripts/run_backtest.py
python scripts/run_live.py
```

The live runner includes a basic auto-exit (stop-loss/take-profit) example.
