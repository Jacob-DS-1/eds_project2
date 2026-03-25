# eds_project2
An academic earth and environmental data science project aiming to predict TREFMXAV_U in Manchester from 2050 to 2080 using machine learning, and answer an associated climate research question.

This project investigates whether monthly maximum near-surface urban temperature (`TREFMXAV_U`) can be predicted across multiple climate scenarios using other projected climate variables.

## Project aims
- inspect and preprocess NetCDF climate scenario data
- aggregate daily data to monthly scale
- build a supervised learning table
- evaluate XGBoost and linear baselines using rolling time-series cross-validation
- generate post-2050 scenario-conditioned predictions

## Repository structure
- `data/` raw, interim, and processed data
- `notebooks/` exploratory and reporting notebooks
- `src/` reusable source code
- `scripts/` runnable pipeline scripts
- `outputs/` figures, tables, and saved models

## Data
Raw NetCDF files are not stored in the repository. Place them in `data/raw/`.

## Reproducibility
Create the environment from `environment.yml` and run the project scripts once implemented.

## Authors
Jacob Woodland, Yuhui Duan, Ruiqi Huang
