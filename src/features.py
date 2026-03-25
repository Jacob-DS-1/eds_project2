import numpy as np
import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # Need to ensure this works for cftime objects as well as normal datetimes
    df["year"] = df["time"].apply(lambda x: x.year)
    df["month"] = df["time"].apply(lambda x: x.month)
    df["monthly_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["monthly_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    return df


def add_wind_speed(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["wind_speed"] = np.sqrt(df["UBOT"] ** 2 + df["VBOT"] ** 2)
    return df
