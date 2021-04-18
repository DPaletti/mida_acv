from pathlib import Path
from typing import List, Dict

from mida_acv.parsing import parse
from mida_acv.preprocessing import remove_incremental_column, simplify_path
from mida_acv.utilities import write_to_csv, to_tsfresh, window_df
from mida_acv.feature_extraction import features
from mida_acv.visualization import visualize_path, visualize_signal, visualize_all
import pandas as pd


def main():
    data_path = "./data"
    simplification_epsilon = 0.000001
    simplified_data_path = "./data/simplified_datasets_" + str(simplification_epsilon)
    resource_path = "./resources"
    ts, weight_series, drivers_series = to_tsfresh(simplified_data_path)
    print(ts)
    print(weight_series)
    print(drivers_series)
    #    rolled_df = window_df(tsfresh_df)
    feat = features(ts, weight_series)
    # data_dict: Dict[str, List[pd.Dataframe]] = remove_incremental_column(
    #    parse(data_path)
    # )
    # data_dict_simplified = simplify_path(data_dict, simplification_epsilon)
    # write_to_csv(simplified_data_path, data_dict_simplified)
    # visualize_all(
    #    "./resources/plots",
    #    "alberto_jessica",
    #    108,
    #    simplification_epsilon,
    #    pd.read_csv(
    #        data_path + "/stem/double/Calibrated_Alberto_Jessica_108_stem.csv"
    #    ),
    #    pd.read_csv(simplified_data_path + "/stem/double/timeseries-0.csv"),
    # )
