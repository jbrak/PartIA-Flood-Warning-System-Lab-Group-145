from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # Cambridge Coordinate

    p = (52.2053, 0.1218)

    # Determine a list of all the stations with 10km of cambridge
    within_radius = stations_within_radius(stations, p, 10.0)

    # Print the names of each inconsistent weather station
    print(sorted([i.name for i in within_radius]))



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()