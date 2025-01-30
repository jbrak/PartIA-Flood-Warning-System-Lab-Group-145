# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from numpy import arcsin, cos, pi

def haversine_distance(x:(float, float),y:(float, float), r:float):
        """Takes an input of 2 coordinates and the radius of the sphere and
        computes the distance between the 2 coordinates"""

        # Convert coordinates into radians
        lat1 = x[0] * pi/180
        lat2 = y[0] * pi/180
        long1 = x[1] * pi/180
        long2 = y[1] * pi/180

        # Calculate the differences between lattitude and longitude
        dlat = ((lat2 - lat1)**2)**0.5
        dlong = ((long2 - long1)**2)**0.5

        # calculate inverse haversine and return the value
        return 2*r*arcsin(((1-cos(dlat) + cos(lat1)*cos(lat2)*(1-cos(dlong)))/2)**0.5)

def stations_by_distance(stations : [MonitoringStation], p : (float, float)):
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
        lst = [(i, haversine_distance(x = p, y = i.coord, r = 6400)) for i in stations]

        # Sorts the list by the second entry, the distance
        return sorted_by_key(x=lst,i=1)

def stations_within_radius(stations:[MonitoringStation], centre:(float, float), r: float):
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