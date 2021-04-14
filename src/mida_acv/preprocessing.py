from typing import List, Dict

import pandas as pd
from rdp import rdp
import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm

from mida_acv.utilities import get_path


def remove_incremental_column(
    data: Dict[str, List[pd.DataFrame]]
) -> Dict[str, List[pd.DataFrame]]:
    for k, v in data.items():
        for i, df in enumerate(v):
            data[k][i] = df.drop(columns=["Unnamed: 0"])
    return data


def simplify_path(
    data: Dict[str, List[pd.DataFrame]], epsilon: float
) -> Dict[str, List[pd.DataFrame]]:
    for k, v in data.items():
        data[k] = Parallel(n_jobs=multiprocessing.cpu_count())(
            delayed(__simplify)(data[k][i], df, epsilon) for i, df in tqdm(enumerate(v))
        )
    return data


def __simplify(data, df, epsilon):
    return data[rdp(get_path(df), epsilon=epsilon, return_mask=True)]
