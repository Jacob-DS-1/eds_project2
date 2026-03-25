import xarray as xr

from src.config import RAW_DATA_DIR, INTERIM_DATA_DIR
from src.data_loading import list_nc_files, load_dataset, get_scenario_name
from src.preprocessing import drop_always_missing_target_cells, aggregate_monthly


def main():
    files = list_nc_files(RAW_DATA_DIR)

    if not files:
        raise FileNotFoundError(
            f"No .nc files found in {RAW_DATA_DIR}. Put your raw NetCDF files there first."
        )

    datasets = []

    for path in files:
        print(f"Loading {path.name}")
        ds = load_dataset(path)
        scenario = get_scenario_name(path)

        ds = drop_always_missing_target_cells(ds)
        ds = ds.expand_dims(scenario=[scenario])
        datasets.append(ds)

        combined = xr.concat(datasets, dim="scenario")
        monthly = aggregate_monthly(combined)

        # Convert MultiIndex cell into regular coordinates so it can be saved to NetCDF
        monthly = monthly.reset_index("cell")

        output_path = INTERIM_DATA_DIR / "monthly_dataset.nc"
        monthly.to_netcdf(output_path)

    print(f"Saved monthly dataset to: {output_path}")


if __name__ == "__main__":
    main()
