import pandas as pd
from src.evaluation import regression_metrics, grouped_regression_metrics


def test_regression_metrics_includes_bias():
    y_true = [1.0, 2.0, 3.0]
    y_pred = [2.0, 2.0, 2.0]
    metrics = regression_metrics(y_true, y_pred)
    assert set(metrics.keys()) == {"rmse", "mae", "r2", "bias"}
    assert abs(metrics["bias"] - 0.0) < 1e-12


def test_grouped_regression_metrics_returns_expected_groups():
    df = pd.DataFrame(
        {
            "scenario": ["003", "003", "004", "004"],
            "y_true": [1.0, 2.0, 3.0, 4.0],
            "y_pred": [1.0, 2.5, 2.0, 5.0],
        }
    )
    out = grouped_regression_metrics(df, ["scenario"], "y_true", "y_pred")
    assert list(out["scenario"]) == ["003", "004"]
    assert list(out["n"]) == [2, 2]
