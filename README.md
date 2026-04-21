# eds_project2
An academic earth and environmental data science project investigating post-2050 changes in monthly maximum near-surface urban temperature (`TREFMXAV_U`) across climate scenarios. The project combines climate-data preprocessing, supervised learning, and post-2050 scenario, seasonal, spatial, and Manchester-focused analysis.

## Research question

How do projected post-2050 increases in `TREFMXAV_U` vary across scenario and season, and are these patterns in Manchester consistent with those across the wider study region? As a supporting analysis, which variables appear most important for explaining projected variation in `TREFMXAV_U`?

## Project aims
- inspect and preprocess NetCDF climate scenario data
- aggregate daily data to monthly scale
- build a supervised learning table
- evaluate XGBoost and linear baselines using rolling time-series cross-validation on pre-2050 data
- fit a final model on pre-2050 data and evaluate on post-2050 rows where `TREFMXAV_U` is available
- analyse post-2050 scenario, seasonal, spatial, and Manchester-focused patterns in predictions

## Repository structure
- `data/` raw, interim, and processed data
- `notebooks/` exploratory and reporting notebooks
- `src/` reusable source code
- `scripts/` runnable pipeline scripts
- `outputs/` figures, tables, and saved models
- `presentation/` contains the final project slide deck

## Data
Raw NetCDF files are not stored in the repository. Place them in `data/raw/`.

## Reproducibility
Create the environment from `environment.yml`, place the raw NetCDF files in `data/raw/`, and then run the notebooks/scripts in workflow order.

Suggested workflow:
1. preprocess and aggregate the raw climate data
2. run `03_modeling_xgboost.ipynb` for model fitting, expanding window validation, ablation, feature-importance analysis, final training, and post-2050 holdout scoring
3. run `04_post2050_predictions.ipynb` for post-2050 evaluation against truth, then scenario, seasonal, spatial, and Manchester-focused analysis

## Key results

- XGBoost outperformed linear and ridge baselines for predicting `TREFMXAV_U` during pre-2050 validation.
- Removing `TREFHT` reduced model performance substantially, showing it is a major predictor, while reduced-model skill remained strong enough to indicate useful contributions from other variables.
- For post-2050 predictions:
    - Post-2050 warming is positive across all scenarios, with stronger increases by 2070–2080 than in 2050–2059.
    - Projected warming is seasonally uneven, with larger increases in late spring, summer, and early autumn than in late autumn and winter.
    - Manchester follows the broader regional warming pattern but remains consistently warmer in absolute terms and shows some seasonal differences in warming magnitude.

## Authors
Jacob Woodland, Yuhui Duan, Ruiqi Huang
