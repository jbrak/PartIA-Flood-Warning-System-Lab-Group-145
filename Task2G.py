import datetime
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.dates


def run():
    # Build list of stations
    stations = build_station_list()

    N = int(
        input(
            f"Please input the number of stations you want to include\nNote that numbers greater than 50 can take a long time\nThe total number of stations is {len(stations)}\n"
        )
    )
    stations = stations[:N]
    # Update latest level data for all stations
    update_water_levels(stations)

    # Initialise risk factors
    risk_factor = {}
    for station in stations:
        risk_factor[station.town] = 0

    i = 0
    # If a station close to a town has rising water level, then add the station's *relative water level* to the town's *rise risk factor*
    for station in stations:
        # Generate the dates and levles for the stations
        dt = 2
        date, level = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt)
        )
        try:
            f = polyfit(date, level, 5)[0]
            f_d = f.deriv()
            if (
                f_d(matplotlib.dates.date2num(date[-1])) > 0
                and station.relative_water_level() is not None
            ):
                risk_factor[station.town] += station.relative_water_level()
            print(f"Progress: {i+1}/{N}")
            i += 1
        except IndexError:
            print(f"Progress: {i+1}/{N}")
            i += 1
            continue

    sorted_risk_factor = sorted(
        risk_factor.items(), key=lambda item: item[1], reverse=True
    )
    i = len(sorted_risk_factor) - 1
    while True:
        if sorted_risk_factor[i][1] != 0:
            min = sorted_risk_factor[i][1]
            break
        i -= 1
    diff_max = sorted_risk_factor[0][1] - min
    for town in sorted_risk_factor:
        if diff_max != 0:
            relative_risk_level = (town[1] - min) / diff_max
            if relative_risk_level < 0.25:
                risk_rating = "\033[34mlow\033[0m"
            elif relative_risk_level >= 0.25 and relative_risk_level < 0.50:
                risk_rating = "\033[33mmoderate\033[0m"
            elif relative_risk_level >= 0.50 and relative_risk_level < 0.75:
                risk_rating = "\033[38;2;255;165;0mhigh\033[0m"
            else:
                risk_rating = "\033[31msevere\033[0m"
        else:
            risk_rating = "low"
        print(f"{town[0]} {risk_rating} {town[1]}")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
