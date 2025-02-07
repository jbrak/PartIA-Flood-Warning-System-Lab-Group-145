# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
plotting data with matplotlib.

"""
import matplotlib.pyplot as plt
from datetime import datetime
from .station import MonitoringStation
from .analysis import polyfit
from matplotlib.dates import date2num
import numpy as np

def plot_water_levels(stations: [MonitoringStation], dates: [[datetime]], levels: [[float]], img=False):
    """A function to produce a plot of water level against time for a particular monitoring station
    Parameters:
        stations : [MonitoringStation] length between 1 and 6
        dates : [[datetime]] length between 1 and 6
        levels : [[float]] length between 1 and 6, length of sublist the same as length of sublist dates
        img : either False if you do not want an image to be returned or the filepath of the image
    returns:
        matlplotlib figure or image
    """

    # Input Validation
    assert len(stations) <= 6
    assert len(levels) == len(stations)
    assert len(dates) == len(levels)
    for i, j in zip(levels, dates):
        assert len(j) == len(i)
    assert (img == False) or (type(img) == str)

    # Calculate the number of plots per column and row
    R = 2
    if len(stations) == 1:
        N = 1
        R = 1
    elif len(stations) % 2 == 1:
        N = len(stations) // 2 + 1
    else:
        N = len(stations) // 2

    # Define the subplot figure
    fig, axs = plt.subplots(nrows=R, ncols=N, figsize=(10, 7))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

    # Generate each individual graph
    for i in range(len(stations)):

        # define the relevent variables for each indvidual plot
        station = stations[i]
        date = dates[i]
        level = levels[i]

        # Determine the location of the plot depending on the grid layout
        if N > 1:
            axis = axs[i // N, i % N]
        elif R == 1:
            axis = axs
        else:
            axis = axs[i]

        # Produces Line Graph
        axis.plot(date, level, color="purple")

        # Adds title of station name
        axis.set_title(station.name)

        # Configures coordinate axes
        axis.set(xlabel="date", ylabel='water level (m)')
        axis.tick_params(labelrotation=45)

        # Draws typical level lines
        axis.plot(date, [station.typical_range[0] for i in range(len(date))], linestyle="dashdot", color="blue")
        axis.plot(date, [station.typical_range[1] for i in range(len(date))], linestyle="dashdot", color="blue")

    # Turns off axis which is not being used
    if (len(stations) % 2 == 1) and (len(stations) != 1):
        axs[-1, -1].axis("off")

    # Ensures plot does not cut off date labels
    fig.tight_layout()

    # Either return the figure or save it as an image
    if img == False:
        return fig, axs, N, R
    else:
        fig.savefig(img)


"""
(0,0) , (0,1), (0,2)
  •       •      •
  •       •      •
(1,0) , (1,1) , (1,2)

i:    0 1 2 3 4 5 
i//3  0 0 0 1 1 1
i%3   0 1 2 0 1 2

so the ith plot is located in subplot (i//3, i%2)
"""

def plot_water_level_with_fit(stations: [MonitoringStation], dates: [[datetime]], levels: [[float]], p:int, img=False):
    """A function to produce a plot of water level against time for a particular monitoring station
        Parameters:
            station : [MonitoringStation] length between 1 and 6
            dates : [[datetime]] length between 1 and 6
            levels : [[float]] length between 1 and 6, length of sublist the same as length of sublist dates
            p : integer
            img : either False if you do not want an image to be returned or the filepath of the image
        returns:
            matlplotlib figure or image
        """

    assert p >= 0

    fig, axs, N, R = plot_water_levels(stations= stations, dates = dates, levels = levels)

    station_regression = []

    # Loops through every item
    for i in range(len(stations)):
        poly, d0 = polyfit(dates = dates[i], levels = levels[i], p = p)
        station_regression.append((stations[i], poly, d0))

        # Determine the location of the plot depending on the grid layout
        if N > 1:
            axis = axs[i // N, i % N]
        elif R == 1:
            axis = axs
        else:
            axis = axs[i]

        # Calculate dates to nums
        x = date2num(dates[i])

        # Calculate the y-values for the trendline
        y = poly(x-d0)

        # Add the trendline to the axis
        axis.plot(dates[i],y, color = "green")

    # Return an image file at the defined path or return the figure objects
    if img == False:
        return fig
    else:
        fig.savefig(img)