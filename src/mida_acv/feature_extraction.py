import pandas as pd
from tsfresh import extract_relevant_features


def features(df: pd.DataFrame, targets) -> pd.DataFrame:

    return extract_relevant_features(
        df,
        targets,
        column_id="id",
        column_sort="Timestamp",
    )
