import pandas as pd
from src.holdout import split_dev_holdout, add_period_labels, add_error_columns


def test_split_dev_holdout_uses_2050_cutoff():
    df = pd.DataFrame({"year": [2049, 2050, 2051]})
    dev_df, holdout_df = split_dev_holdout(df, year_col="year", cutoff_year=2050)
    assert dev_df["year"].tolist() == [2049]
    assert holdout_df["year"].tolist() == [2050, 2051]


def test_add_period_labels_assigns_seasons():
    df = pd.DataFrame({"year": [2050, 2050, 2050], "month": [1, 4, 8]})
    out = add_period_labels(df)
    assert out["season"].tolist() == ["DJF", "MAM", "JJA"]


def test_add_error_columns():
    df = pd.DataFrame(
        {
            "TREFMXAV_U_true": [10.0, 12.0],
            "pred_TREFMXAV_U": [11.0, 11.5],
        }
    )
    out = add_error_columns(df)
    assert out["error"].tolist() == [1.0, -0.5]
    assert out["abs_error"].tolist() == [1.0, 0.5]
