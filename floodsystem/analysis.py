# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
analysing the station data.

"""

import numpy
from matplotlib.dates import date2num
from datetime import datetime

def polyfit(dates:[datetime], levels:[float], p:int):
    """A function to perform least squares fit of dates and levels to form a trendline using numpy
        Parameters:
            dates : [datetime]
            levels : [float]
            p : int
        returns:
            numpy.poly1d object of trendline
            the shift of the date (time) axis.
        """

    num_dates = date2num(dates)

    d0 = num_dates[0]

    num_dates = num_dates - d0

    coeff = numpy.polyfit(num_dates, levels, p)

    return numpy.poly1d(coeff), d0