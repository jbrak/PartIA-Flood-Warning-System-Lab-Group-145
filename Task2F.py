import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    # Find top 5 stations with the greatest relative water levels
    stations1 = stations_highest_rel_level(stations, 4)

    # Create empty lists
    dates = []
    levels = []

    # Generate the dates and levels for the stations
    for station in stations1:
        dt = 2
        date, level = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt)
        )

        dates.append(date)
        levels.append(level)

    # Run the function to generate the figure
    plot_water_level_with_fit(stations1, dates, levels, 4)

    # Show the figure
    plt.show()


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
