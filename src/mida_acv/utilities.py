from pathlib import Path
from typing import Tuple, List, Dict

import pandas as pd
import numpy as np


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
