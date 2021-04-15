from typing import Dict, List
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def pca(df: pd.DataFrame):
    df = df.drop(["Driver", "Weight", "Placement", "Placement", "Confidence"])
    df.fillna(0)
    pass
