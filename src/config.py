from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
MODELS_DIR = OUTPUTS_DIR / "models"

TARGET = "TREFMXAV_U"

FOLDS = [
    {"train_end": "2029-12-01", "val_start": "2030-01-01", "val_end": "2034-12-01"},
    {"train_end": "2034-12-01", "val_start": "2035-01-01", "val_end": "2039-12-01"},
    {"train_end": "2039-12-01", "val_start": "2040-01-01", "val_end": "2044-12-01"},
    {"train_end": "2044-12-01", "val_start": "2045-01-01", "val_end": "2049-12-01"},
]
