# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the plot module"""

import datetime
import matplotlib as plt
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import numpy as np

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


def test_plot_water_level_with_fit():
    """Unit test for plot_water_levels with fit functino"""

    stations = build_station_list()

    # Make sure that p is greater than 0
    fig = plot_water_level_with_fit(stations[:6],
                    [[datetime.datetime(day=1, month=1, year=1999) for i in range(10)] for i in range(6)],
                    [[1.01 for i in range(10)] for i in range(6)], p=0)

    # Ensure output is the correct type
    assert type(fig) == plt.figure.Figure
