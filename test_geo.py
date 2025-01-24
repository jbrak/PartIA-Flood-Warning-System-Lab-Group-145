# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

import datetime

from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine_distance, stations_by_distance

def test_haversine_distance():
    """Unit test for haversine_distance function"""
    london = (51.5007, 0.1246)
    new_york = (40.6892, 74.0445)
    r = 6371

    d = float(haversine_distance(london, new_york, r))

    assert round(d,1) == 5574.8

def test_stations_by_distance():
    """Unit test for the stations_by_distance function"""

    # Build the list of stations
    stations = build_station_list()

    # Built the list of distances from cambridge city center for the stations
    distances = stations_by_distance(stations=stations, p=(52.2053, 0.1218))

    # Check that the closest station is in cambridge
    assert distances[0][0].town == "Cambridge"

    # Check that the distance of each item is less than the item after it
    for i in range(len(distances)-1):
        assert distances[i][1] <= distances[i+1][1]