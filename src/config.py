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
    {"train_end_year": 2029, "val_start_year": 2030, "val_end_year": 2034},
    {"train_end_year": 2034, "val_start_year": 2035, "val_end_year": 2039},
    {"train_end_year": 2039, "val_start_year": 2040, "val_end_year": 2044},
    {"train_end_year": 2044, "val_start_year": 2045, "val_end_year": 2049},
]

POST2050_HOLDOUT_PREDICTIONS = TABLES_DIR / "post2050_holdout_predictions.csv"
POST2050_METRICS_OVERALL = TABLES_DIR / "post2050_metrics_overall.csv"
POST2050_METRICS_BY_SCENARIO = TABLES_DIR / "post2050_metrics_by_scenario.csv"
POST2050_METRICS_BY_SEASON = TABLES_DIR / "post2050_metrics_by_season.csv"
POST2050_METRICS_BY_SCENARIO_SEASON = TABLES_DIR / "post2050_metrics_by_scenario_season.csv"
POST2050_METRICS_BY_YEAR = TABLES_DIR / "post2050_metrics_by_year.csv"
