import numpy as np
import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"])
    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.month
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    return df


def add_wind_speed(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["wind_speed"] = np.sqrt(df["UBOT"] ** 2 + df["VBOT"] ** 2)
    return df
