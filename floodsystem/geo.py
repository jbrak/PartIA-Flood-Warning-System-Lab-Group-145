# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from numpy import arcsin, cos, pi


def haversine_distance(x: (float, float), y: (float, float), r: float):
    """Takes an input of 2 coordinates and the radius of the sphere and
    computes the distance between the 2 coordinates"""

    # Convert coordinates into radians
    lat1 = x[0] * pi / 180
    lat2 = y[0] * pi / 180
    long1 = x[1] * pi / 180
    long2 = y[1] * pi / 180

    # Calculate the differences between lattitude and longitude
    dlat = ((lat2 - lat1) ** 2) ** 0.5
    dlong = ((long2 - long1) ** 2) ** 0.5

    # calculate inverse haversine and return the value
    return (
        2
        * r
        * arcsin(
            ((1 - cos(dlat) + cos(lat1) * cos(lat2) * (1 - cos(dlong))) / 2) ** 0.5
        )
    )


def stations_by_distance(stations: [MonitoringStation], p: (float, float)):
    """Takes an input of a list of station objects and a coordinate p and returns
    a list of tuples in the format (station, distance) where the distance is the
    distance between p and the station
    Parameters:
            stations : [MonitoringStation]
            p : (float, float)
    Return:
            [(MonitoringStation, float)]
    """

    # Generates the list of tuples
    lst = [(i, haversine_distance(x=p, y=i.coord, r=6400)) for i in stations]

    # Sorts the list by the second entry, the distance
    return sorted_by_key(x=lst, i=1)


def stations_within_radius(
    stations: [MonitoringStation], centre: (float, float), r: float
):
    """Takes an input of a list of station objects and a coordinate p and a radius r and
    returns a list of stations that are found within those radius
    Parameters:
            stations : [MonitoringStation]
            centre : (float, float)
            r : float
    Return:
            [MonitoringStation]
    """

    distances = stations_by_distance(stations, centre)

    return [i[0] for i in distances if i[1] < r]


def rivers_with_station(stations):
    """
    Takes a list of station objects, returns a set with the names of the rivers with a monitoring station.
    Parameters:
            stations : [MonitoringStation]
    Return:
            {MonitoringStation}
    """
    return {i.river for i in stations}


def stations_by_river(stations):
    """
    Takes a list of station objects, returns a dict that maps river names (the ‘key’) to a list of station objects on a given river.
    Parameters:
            stations : [MonitoringStation]
    Return:
            {str : [MonitoringStation]}
    """
    rivers = rivers_with_station(stations)
    res_dict = {}
    for i in rivers:
        tmp_stations = []
        for j in stations:
            if i == j.river:
                tmp_stations.append(j)
            res_dict.update({i: tmp_stations})
    return res_dict


def rivers_by_station_number(stations, N):
    """
    Takes a list of station objects and an integer N, return a list of (river name, number of stations) tuples, sorted by the number of stations. In the case that there are more rivers with the same number of stations as the N th entry, include these rivers in the list.
    Parameters:
            stations : [MonitoringStation]
            N : int
    Return:
            [(str, int)]
    """
    rivers_dict = stations_by_river(stations)
    rivers_list_sorted = sorted(
        rivers_dict.items(), key=lambda item: item[1].__len__(), reverse=True
    )
    res_tuple = []
    N = len(rivers_list_sorted) if N > len(rivers_list_sorted) else N
    for i in range(N):
        res_tuple.append((rivers_list_sorted[i][0], len(rivers_list_sorted[i][1])))
    for i in range(N, len(rivers_list_sorted)):
        if len(rivers_list_sorted[i][1]) == len(rivers_list_sorted[N - 1][1]):
            res_tuple.append((rivers_list_sorted[i][0], len(rivers_list_sorted[i][1])))
        else:
            break
    return res_tuple
