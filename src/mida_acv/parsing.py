from pathlib import Path
from typing import Iterable, List, Optional
import pandas as pd

from mida_acv.driver_enum import Driver
from mida_acv.sensor_position_enum import SensorPosition


def parse(data_path: str):
    data_dict = {}
    for sensor_position in list(SensorPosition):
        for driver_number in Driver:
            data_dict[
                str(sensor_position.name).lower()
                + "-"
                + str(driver_number.name).lower()
            ] = __parse_dir(Path(data_path), sensor_position, driver_number)
    return data_dict


def __parse_dir(data_path: Path, sensor_position: SensorPosition, driver: Driver):
    out = []
    for file_path in data_path.joinpath(
        str(sensor_position.name).lower(), str(driver.name).lower()
    ).iterdir():
        out.append(pd.read_csv(file_path))
    return out
