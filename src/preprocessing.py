import xarray as xr


def drop_always_missing_target_cells(ds: xr.Dataset, target: str = "TREFMXAV_U") -> xr.Dataset:
    valid_cells = ds[target].notnull().any(dim="time")
    ds = ds.stack(cell=("lat", "lon"))
    valid_cells = valid_cells.stack(cell=("lat", "lon"))
    ds = ds.isel(cell=valid_cells.values)
    return ds


def aggregate_monthly(ds: xr.Dataset) -> xr.Dataset:
    monthly = xr.Dataset({
        "TREFMXAV_U": ds["TREFMXAV_U"].resample(time="MS").mean(),
        "TREFHT": ds["TREFHT"].resample(time="MS").mean(),
        "FLNS": ds["FLNS"].resample(time="MS").mean(),
        "FSNS": ds["FSNS"].resample(time="MS").mean(),
        "PRECT": ds["PRECT"].resample(time="MS").sum(),
        "PRSN": ds["PRSN"].resample(time="MS").sum(),
        "QBOT": ds["QBOT"].resample(time="MS").mean(),
        "UBOT": ds["UBOT"].resample(time="MS").mean(),
        "VBOT": ds["VBOT"].resample(time="MS").mean(),
    })
    return monthly
