from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def bias(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float(np.mean(y_pred - y_true))


def rmse(y_true, y_pred) -> float:
    return float(mean_squared_error(y_true, y_pred) ** 0.5)


def regression_metrics(y_true, y_pred) -> dict:
    return {
        "rmse": rmse(y_true, y_pred),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "r2": float(r2_score(y_true, y_pred)),
        "bias": bias(y_true, y_pred),
    }


def grouped_regression_metrics(
    df: pd.DataFrame,
    group_cols: list[str],
    y_true_col: str,
    y_pred_col: str,
) -> pd.DataFrame:
    rows = []
    for keys, group in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        metrics = regression_metrics(group[y_true_col], group[y_pred_col])
        row = {col: key for col, key in zip(group_cols, keys)}
        row["n"] = int(len(group))
        row.update(metrics)
        rows.append(row)
    return pd.DataFrame(rows).sort_values(group_cols).reset_index(drop=True)
