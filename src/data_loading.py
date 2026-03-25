from pathlib import Path
import xarray as xr


def list_nc_files(raw_data_dir: Path):
    return sorted(raw_data_dir.glob("*.nc"))


def load_dataset(path: Path) -> xr.Dataset:
    return xr.open_dataset(path)


def get_scenario_name(path: Path) -> str:
    return path.stem.split("_")[0]
