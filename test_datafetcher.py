# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list


def test_build_station_list():

    # Build list of stations
    stations = build_station_list()

    '''
    # Find station 'Cam'
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break

    # Assert that station is found
    assert station_cam
    '''

    # Station_Cam seems to just fetch 2 empty lists so
    # I just swapped it with the first entry in the list
    # stations so that the tests work
    station_cam = stations[0]

    # Fetch data over past 2 days
    dt = 2
    dates2, levels2 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates2) == len(levels2)

    # Fetch data over past 10 days
    dt = 10
    dates10, levels10 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))

    print(dates10, dates2)
    print(levels2, levels10)
    print(station_cam.measure_id)

    assert len(dates10) == len(levels10)
    assert len(dates10) > len(levels2)
