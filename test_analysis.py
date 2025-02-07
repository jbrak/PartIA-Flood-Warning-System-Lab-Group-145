# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module"""

from floodsystem.analysis import polyfit
import numpy as np
from matplotlib.dates import num2date

def test_polyfit():
    """Unit test for plot_water_levels function"""
    x = np.linspace(1,100,100)
    y = x**2

    poly, d0 = polyfit(num2date(x), y, 2)

    assert d0 == 1
    assert round(poly(2-d0),5) == 4.00000
    assert round(poly(9-d0),5) == 81.00000