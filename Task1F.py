from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # Determine a list of all the stations with inconsistent typical range data
    inconsistent = inconsistent_typical_range_stations(build_station_list())

    # Print the names of each inconsistent weather station
    print([i.name for i in inconsistent])



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()