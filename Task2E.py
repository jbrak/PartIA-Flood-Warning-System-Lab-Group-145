# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

### Rought demo script while waiting for S.Ding to complete task 2C

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import matplotlib.pyplot as plt

def run():

    # Build list of stations
    stations = build_station_list()

    # Station name to find
    stations1 = stations[:5]

    # Create empty lists
    dates = []
    levels = []

    # Generate the dates and levles for the stations
    for station in stations1:
        dt = 5
        date, level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        dates.append(date)
        levels.append(level)

    # Generate the figure
    plot_water_levels(stations1, dates, levels)

    # Show the figure
    plt.show()


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
