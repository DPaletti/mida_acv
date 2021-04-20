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
    visualize_signal(
        pd.read_csv(
            data_path + "/stem/single/Calibrated_Davide_Conficconi_115_stem.csv"
        ),
        "Ax",
        "m/s^2",
        "Acceleration along x axis recorded from the stem",
        (
            pd.read_csv(
                data_path + "/deck/single/Calibrated_Davide_Conficconi_115_deck.csv"
            ),
            "Acceleration along x axis recorded from the deck",
        ),
    ).show()
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
