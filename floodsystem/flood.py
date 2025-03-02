from .station import MonitoringStation


def stations_level_over_threshold(stations: [MonitoringStation], tol: float):
    return_list = []
    for station in stations:
        relative = station.relative_water_level()
        if relative is not None and relative > tol:
            return_list.append((station, relative))
    return sorted(return_list, key=lambda Tuple: Tuple[1], reverse=True)


def stations_highest_rel_level(stations: [MonitoringStation], N: int):
    return_list = []
    for station in stations:
        relative = station.relative_water_level()
        if relative is not None:
            return_list.append((station, relative))
    return_list = sorted(return_list, key=lambda Tuple: Tuple[1], reverse=True)
    final_return_list = []
    for i in range(N):
        final_return_list.append(return_list[i][0])
    return final_return_list
