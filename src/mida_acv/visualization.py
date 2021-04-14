from pathlib import Path

import pandas as pd
import plotly.graph_objects as go


def visualize_path(df: pd.DataFrame, data_path: str, df_full: pd.DataFrame = None):
    fig = go.Figure(
        go.Scattermapbox(
            mode="markers+lines",
            lon=df["Longitude"],
            lat=df["Latitude"],
            marker={"size": 10},
        )
    )
    if df_full is not None:
        fig.add_trace(
            go.Scattermapbox(
                mode="markers+lines",
                lon=df_full["Longitude"],
                lat=df_full["Latitude"],
                marker={"size": 3},
            )
        )

    fig.update_layout(
        margin={"l": 0, "t": 0, "b": 0, "r": 0},
        mapbox={
            "style": "stamen-terrain",
            "accesstoken": Path(data_path).joinpath(".mapbox_token").read_text(),
        },
    )
    fig.show()
