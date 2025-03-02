# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the plot module"""

import datetime
import matplotlib as plt
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import numpy as np
import pytest

def test_plot_water_levels():
    """Unit test for plot_water_levels function"""
    stations = build_station_list()

    # Ensure the function produces a graph

    fig, axs, N, R = plot_water_levels(stations[:6],
                [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in range(6)],
                [[1.01 for i in range(10)] for i in range(6)])

    # Ensure outputs are correct types
    assert type(fig) == plt.figure.Figure
    assert type(axs) == np.ndarray
    assert type(N) == int
    assert type(R) == int

    # Check error triggered when too many stations inputted
    with pytest.raises(AssertionError):
        plot_water_levels(stations[:7],
                          [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in range(6)],
                          [[1.01 for i in range(10)] for i in range(6)])

    # Check error triggered when the length of dates is different to that of stations and levels
    with pytest.raises(AssertionError):
        plot_water_levels(stations[:6],
                        [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in range(7)],
                        [[1.01 for i in range(10)] for i in range(6)])

    # Check error triggered when the length of levels is different to that of stations and dates
    with pytest.raises(AssertionError):
        plot_water_levels(stations[:6],
                        [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in range(6)],
                        [[1.01 for i in range(10)] for i in range(7)])

    # Check error triggered when the length of levels sublist is different to that of dates sublist
    with pytest.raises(AssertionError):
        plot_water_levels(stations[:6],
                        [[datetime.datetime(day=1, month=1, year=1999) for i in range(11)] for i in range(6)],
                        [[1.01 for i in range(10)] for i in range(6)])

    # Check error triggered when img is not False or a string
    with pytest.raises(AssertionError):
        plot_water_levels(stations[:6],
                        [[datetime.datetime(day=1, month=1, year=1999) for i in range(11)] for i in range(6)],
                        [[1.01 for i in range(10)] for i in range(6)], img=90)



def test_plot_water_level_with_fit():
    """Unit test for plot_water_levels with fit functino"""

    stations = build_station_list()

    # Make sure that p is greater than 0
    fig = plot_water_level_with_fit(stations[:6],
                    [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in range(6)],
                    [[1.01 for i in range(10)] for i in range(6)], p=0)

    # Ensure output is the correct type
    assert type(fig) == plt.figure.Figure

    # Check error triggered when p is less than 0
    with pytest.raises(AssertionError):
        fig = plot_water_level_with_fit(stations[:6],
                                        [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in
                                         range(6)],
                                        [[1.01 for i in range(10)] for i in range(6)], p=-5)

