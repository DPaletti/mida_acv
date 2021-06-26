from pathlib import Path
from typing import Tuple, List

import pandas as pd
import plotly.graph_objects as go


def visualize_path(df: pd.DataFrame, mapbox_token_path: str, *args):
    fig = go.Figure(
        go.Scattermapbox(
            mode="lines",
            lon=df["Longitude"],
            lat=df["Latitude"],
            marker={"size": 5, "color": "red"},
        )
    )
    for _df in args:
        fig.add_trace(
            go.Scattermapbox(
                mode="lines",
                lon=_df["Longitude"],
                lat=_df["Latitude"],
                marker={"size": 5},
            )
        )

    fig.update_layout(
        margin={"l": 0, "t": 0, "b": 0, "r": 0},
        mapbox={
            "style": "stamen-terrain",
            "accesstoken": Path(mapbox_token_path)
            .joinpath(".mapbox_token")
            .read_text(),
        },
    )
    fig.show()


def visualize_signal(
    df: pd.DataFrame, signal: str, unit: str, label, *args: Tuple[pd.DataFrame, str]
):
    fig = go.Figure(
        go.Scatter(
            mode="markers+lines",
            x=df["Timestamp"],
            y=df[signal if signal not in {"A", "G", "Jerk_"} else signal + "x"],
            marker={"size": 3},
            name=label,
        )
    )

    fig.update_layout(
        xaxis={"title": "Time (s)"},
        yaxis={"title": signal.replace("_", "") + " (" + unit + ")"},
        width=1920,
        height=1080,
        font=dict(size=18),
        template="plotly_white",
    )

    if signal not in {"A", "G", "Jerk_"}:
        for _df, _label in args:
            fig.add_trace(
                go.Scatter(
                    mode="markers+lines",
                    x=_df["Timestamp"],
                    y=_df[signal],
                    marker={"size": 3},
                    name=_label,
                )
            )
    else:
        dfs: List[pd.DataFrame] = []
        labels: List[str] = []
        for t in args:
            dfs.append(t[0])
            labels.append(t[1])
        for _df, _label, axis in zip(dfs, labels, ["y", "z"]):
            fig.add_trace(
                go.Scatter(
                    mode="markers+lines",
                    x=_df["Timestamp"],
                    y=_df["Speed" if signal == "Speed" else signal + axis],
                    marker={"size": 3},
                    name=_label,
                )
            )
    return fig


def visualize_all(
    plot_path: str,
    driver: str,
    weight: int,
    simplification_epsilon: float,
    df: pd.DataFrame,
    simplified_df: pd.DataFrame,
):
    for to_visualize, unit, full_name in zip(
        ["Speed", "A", "G", "Jerk_"],
        ["km/h", "m/s^2", "grad", "m/s^3"],
        ["Speed", "Acceleration", "Orientation", "Jerk"],
    ):
        if to_visualize == "Speed":
            visualize_signal(
                df, "Speed", unit, full_name + " on the full path"
            ).write_image(
                str(
                    Path(plot_path).joinpath(
                        full_name.lower()
                        + "_full_"
                        + driver
                        + "_"
                        + str(weight)
                        + ".png"
                    )
                ),
            )
            visualize_signal(
                df,
                "Speed",
                "km/h",
                "Speed on the full path",
                (simplified_df, "Speed on the simplified path"),
            ).write_image(
                str(
                    Path(plot_path).joinpath(
                        "speed_full_simplified_"
                        + driver
                        + str(weight)
                        + "_"
                        + str(simplification_epsilon)
                        + ".png"
                    )
                )
            )
        else:
            visualize_signal(
                df,
                to_visualize,
                unit,
                "Pitch" if full_name == "Orientation" else full_name + " along x axis",
                (
                    df,
                    "Yaw"
                    if full_name == "Orientation"
                    else full_name + " along y axis",
                ),
                (
                    df,
                    "Roll"
                    if full_name == "Orientation"
                    else full_name + " along z axis",
                ),
            ).write_image(
                str(
                    Path(plot_path).joinpath(
                        full_name.lower()
                        + "_full_"
                        + driver
                        + "_"
                        + str(weight)
                        + ".png"
                    )
                )
            )
            visualize_signal(
                df,
                to_visualize + "x",
                unit,
                "Pitch" if full_name == "Orientation" else full_name + " along x axis",
                (
                    simplified_df,
                    (
                        "Pitch "
                        if full_name == "Orientation"
                        else (full_name + " along x axis ")
                    )
                    + "on the simplified path",
                ),
            ).write_image(
                str(
                    Path(plot_path).joinpath(
                        (
                            (full_name.lower() + "_pitch")
                            if full_name == "Orientation"
                            else (full_name + "x")
                        )
                        + "_"
                        + driver
                        + "_"
                        + str(weight)
                        + "_"
                        + str(simplification_epsilon)
                        + ".png"
                    )
                )
            )
            visualize_signal(
                df,
                to_visualize + "y",
                unit,
                "Yaw" if full_name == "Orientation" else full_name + " along y axis",
                (
                    simplified_df,
                    (
                        "Yaw "
                        if full_name == "Orientation"
                        else (full_name + " along y axis ")
                    )
                    + "on the simplified path",
                ),
            ).write_image(
                str(
                    Path(plot_path).joinpath(
                        (
                            (full_name.lower() + "_yaw")
                            if full_name == "Orientation"
                            else (full_name + "y")
                        )
                        + "_"
                        + driver
                        + "_"
                        + str(weight)
                        + "_"
                        + str(simplification_epsilon)
                        + ".png"
                    )
                )
            )
            visualize_signal(
                df,
                to_visualize + "z",
                unit,
                "Roll" if full_name == "Orientation" else full_name + " along z axis",
                (
                    simplified_df,
                    (
                        "Roll "
                        if full_name == "Orientation"
                        else (full_name + " along z axis ")
                    )
                    + "on the simplified path",
                ),
            ).write_image(
                str(
                    Path(plot_path).joinpath(
                        (
                            full_name.lower() + "_roll"
                            if full_name == "Orientation"
                            else (full_name + "z")
                        )
                        + "_"
                        + driver
                        + "_"
                        + str(weight)
                        + "_"
                        + str(simplification_epsilon)
                        + ".png"
                    )
                )
            )
