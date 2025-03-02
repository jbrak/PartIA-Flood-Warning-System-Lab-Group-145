# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import matplotlib.pyplot as plt
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    # Build list of stations
    stations = build_station_list()

    # Update stations water levels
    update_water_levels(stations)

    # Find top 5 stations with the greatest relative water levels
    stations1 = stations_highest_rel_level(stations, 5)

    # Create empty lists
    dates = []
    levels = []

    # Generate the dates and levels for the stations
    for station in stations1:
        dt = 10
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
