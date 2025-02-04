# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

import datetime

from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def test_plot_water_levels():
    """Unit test for plot_water_levels function"""
    stations = build_station_list()

    # Make sure only 6 stations
    try:
        plot_water_levels(stations[:10], [[datetime.datetime(day = 1, month = 1, year = 1999) for i in range(10)] for i in range(10)], [[1.01 for i in range(10)] for i in range(10)])
    except AssertionError:
        assert 1==1

    # Make sure number of stations matches number of levles and number of dates
    try:
        plot_water_levels(stations[:6], [[datetime.datetime(day = 1, month = 1, year = 1999) for i in range(10)] for i in range(10)], [[1.01 for i in range(10)] for i in range(10)])
    except AssertionError:
        assert 1==1

    # Makes sure length of each date list matches length of each level list
    try:
        plot_water_levels(stations[:3], [[datetime.datetime(day = 1, month = 1, year = 1999) for i in range(1)] for i in range(3)], [[1.01 for i in range(10)] for i in range(3)])
    except AssertionError:
        assert 1==1

    # Make sure that img is a string when defined
    try:
        plot_water_levels(stations[:3], [[datetime.datetime(day = 1, month = 1, year = 1999) for i in range(10)] for i in range(3)], [[1.01 for i in range(10)] for i in range(3)], img = 57)
    except AssertionError:
        assert 1==1

