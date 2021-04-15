from typing import List, Dict

from mida_acv.parsing import parse
from mida_acv.preprocessing import remove_incremental_column, simplify_path
from mida_acv.utilities import write_to_csv
import pandas as pd


def main():
    data_path = "./data"
    resource_path = "./resources/simplified_datasets"
    data_dict: Dict[str, List[pd.Dataframe]] = remove_incremental_column(
        parse(data_path)
    )
    data_dict_simplified = simplify_path(data_dict, 0.000001)
    write_to_csv(resource_path, data_dict_simplified)
    # visualize_path(
    #    data_dict_simplified["stem-double"][0], data_path, data_dict["stem-double"][0]
    # )


main()
