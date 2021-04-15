from pathlib import Path
from typing import List, Dict

from mida_acv.parsing import parse
from mida_acv.preprocessing import remove_incremental_column, simplify_path
from mida_acv.utilities import write_to_csv
from mida_acv.visualization import visualize_path, visualize_signal, visualize_all
import pandas as pd


def main():
    data_path = "./data"
    simplified_data_path = "./data/simplified_datasets"
    resource_path = "./resources/simplified_datasets"
    # data_dict: Dict[str, List[pd.Dataframe]] = remove_incremental_column(
    #    parse(data_path)
    # )
    # data_dict_simplified = simplify_path(data_dict, 0.000001)
    # write_to_csv(resource_path, data_dict_simplified)
    visualize_all(
        "./resources/plots",
        "leoni",
        35,
        pd.read_csv(
            data_path + "/stem/single_driver/Calibrated_Jessica_Leoni_35_stem.csv"
        ),
        pd.read_csv(simplified_data_path + "/stem/single/timeseries-12.csv"),
    )
