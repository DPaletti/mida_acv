from pathlib import Path
from typing import Tuple, List, Dict

import pandas as pd
import numpy as np
from tsfresh.utilities.dataframe_functions import roll_time_series


def get_path(df: pd.DataFrame) -> np.array:
    out = []
    for index, row in df.iterrows():
        out.append((row["Latitude"], row["Longitude"]))
    return np.array(out)


def write_to_csv(path: str, data: Dict[str, List[pd.DataFrame]]) -> None:
    full_path: Path
    for k, v in data.items():
        full_path = Path(path).joinpath(k[: k.find("-")], k[k.find("-") + 1 :])
        full_path.mkdir(parents=True, exist_ok=True)
        for index, df in enumerate(v):
            df.to_csv(full_path.joinpath("timeseries-" + str(index) + ".csv").open("w"))


def to_tsfresh(data_path: str) -> Tuple[pd.DataFrame, pd.Series, pd.Series]:
    df = pd.DataFrame()
    weight_series = pd.Series()
    drivers_series = pd.Series()
    temp_df: pd.DataFrame
    # ident: str = ""
    i: int = 0
    for placement in {"deck", "stem"}:
        for driver_number in {"single", "double"}:
            for ds in Path(data_path).joinpath(placement, driver_number).iterdir():
                temp_df = pd.read_csv(str(ds))
                weight = temp_df["Weight"][0]
                # ident = placement + "_" + driver_number + "_" + temp_df["Driver"][0]
                temp_df = temp_df.assign(id=i)
                temp_df = temp_df.drop(
                    ["Unnamed: 0", "Driver", "Weight", "Placement"], axis=1
                )
                df = df.append(temp_df)
                weight_series.loc[i] = weight
                drivers_series.loc[i] = 0 if driver_number == "single" else 1
                i += 1
    return df.fillna(0), weight_series, drivers_series


def window_df(df: pd.DataFrame):
    print(df)
    return roll_time_series(
        df, column_id="id", column_sort="Timestamp", column_kind=None
    )
