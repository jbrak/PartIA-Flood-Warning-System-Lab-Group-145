from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Built list of stations with distances
    distance = stations_by_distance(stations=stations, p=(52.2053, 0.1218))

    # find the top and bottom 10 items in the list
    top10 = distance[0:10]
    bottom10 = distance[-10:]

    print("\nClosest 10:")
    for i in top10:
        print((i[0].name, i[0].town, i[1]))

    print("\nFurthest 10:")
    for i in bottom10:
        print((i[0].name, i[0].town, i[1]))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
