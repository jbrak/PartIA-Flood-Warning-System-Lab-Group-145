# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

import datetime

from numpy import seterrcall

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import (
    haversine_distance,
    stations_by_distance,
    stations_within_radius,
)
from floodsystem.geo import (
    rivers_with_station,
    stations_by_river,
    rivers_by_station_number,
)


def test_haversine_distance():
    """Unit test for haversine_distance function"""
    london = (51.5007, 0.1246)
    new_york = (40.6892, 74.0445)
    r = 6371

    d = float(haversine_distance(london, new_york, r))

    assert round(d, 1) == 5574.8


def test_stations_by_distance():
    """Unit test for the stations_by_distance function"""

    # Build the list of stations
    stations = build_station_list()

    # Built the list of distances from cambridge city center for the stations
    distances = stations_by_distance(stations=stations, p=(52.2053, 0.1218))

    # Check that the closest station is in cambridge
    assert distances[0][0].town == "Cambridge"

    # Check that the distance of each item is less than the item after it
    for i in range(len(distances) - 1):
        assert distances[i][1] <= distances[i + 1][1]


def test_stations_within_radius():
    """Unit test for the stations_within_radius function"""

    # Build the list of stations
    stations = build_station_list()

    gaw_bridge = stations_within_radius(
        stations=stations, centre=(50.976043, -2.793549), r=0.01
    )

    # Check there are no stations within 100km of New York
    assert (
        len(
            stations_within_radius(
                stations=stations, centre=(40.6892, 74.0445), r=100.0
            )
        )
        == 0
    )

    # Check there is only one station in the list
    assert len(gaw_bridge) == 1

    # Check that that station is Gaw Bridge
    assert gaw_bridge[0].name == "Gaw Bridge"


def test_rivers_with_station():
    """Unit test for the rivers_with_station function"""

    # Build the list of stations
    stations = build_station_list()

    # Call function to return set of rivers with stations
    rivers = rivers_with_station(stations)

    # Check if returned container is a set
    assert isinstance(rivers, set)

    # Check that River Cam is in the set
    assert "River Cam" in rivers


def test_stations_by_river():
    """Unit test for the rivers_with_station function"""

    # Create the list of test stations
    stations = [
        MonitoringStation(
            None, None, "test station 1", None, None, "test river", "test town"
        ),
        MonitoringStation(
            None, None, "test station 2", None, None, "test river", "test town"
        ),
        MonitoringStation(
            None, None, "test station 3", None, None, "test river", "test town"
        ),
    ]

    # Get the dictionary
    test_disc = stations_by_river(stations)

    assert test_disc["test river"] == stations


def test_rivers_by_station_number():
    """Unit test for the rivers_by_station_number function"""

    # Create the list of test stations
    stations = [
        MonitoringStation(
            None, None, "test station 1", None, None, "test river 1", "test town"
        ),
        MonitoringStation(
            None, None, "test station 2", None, None, "test river 1", "test town"
        ),
        MonitoringStation(
            None, None, "test station 3", None, None, "test river 2", "test town"
        ),
    ]

    test_tuple = rivers_by_station_number(stations, 2)

    assert test_tuple[0] == ("test river 1", 2)
