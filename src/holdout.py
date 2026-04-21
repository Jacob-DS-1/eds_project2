from __future__ import annotations

import pandas as pd


def split_dev_holdout(
    df: pd.DataFrame,
    year_col: str = "year",
    cutoff_year: int = 2050,
):
    dev_df = df[df[year_col] < cutoff_year].copy()
    holdout_df = df[df[year_col] >= cutoff_year].copy()
    return dev_df, holdout_df


def add_period_labels(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    month_to_season = {
        12: "DJF", 1: "DJF", 2: "DJF",
        3: "MAM", 4: "MAM", 5: "MAM",
        6: "JJA", 7: "JJA", 8: "JJA",
        9: "SON", 10: "SON", 11: "SON",
    }
    out["season"] = out["month"].map(month_to_season)
    out["decade"] = (out["year"] // 10) * 10
    return out


def add_error_columns(
    df: pd.DataFrame,
    y_true_col: str = "TREFMXAV_U_true",
    y_pred_col: str = "pred_TREFMXAV_U",
) -> pd.DataFrame:
    out = df.copy()
    out["error"] = out[y_pred_col] - out[y_true_col]
    out["abs_error"] = out["error"].abs()
    out["squared_error"] = out["error"] ** 2
    return out
