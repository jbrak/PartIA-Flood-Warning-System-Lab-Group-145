from floodsystem.stationdata import build_station_list
import floodsystem.geo


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    rivers_set = floodsystem.geo.rivers_with_station(stations)
    rivers = list(rivers_set)
    rivers.sort()
    rivers = rivers[:10]
    print(f"{len(rivers_set)} stations. First 10 - {rivers}")

    rivers_dict = floodsystem.geo.stations_by_river(stations)
    rivers_dict["River Aire"].sort(key=lambda river: river.name)
    rivers_dict["River Cam"].sort(key=lambda river: river.name)
    rivers_dict["River Thames"].sort(key=lambda river: river.name)

    print("\nStations on River Aire:")
    for i in rivers_dict["River Aire"]:
        print(i.name, end=", ")
    print("\n\nStations on River Cam:")
    for i in rivers_dict["River Cam"]:
        print(i.name, end=", ")
    print("\n\nStations on River Thames:")
    for i in rivers_dict["River Thames"]:
        print(i.name, end=", ")


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
