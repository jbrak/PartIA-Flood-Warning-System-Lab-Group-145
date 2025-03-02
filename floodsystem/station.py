# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(
        self, station_id, measure_id, label, coord, typical_range, river, town
    ):
        """Create a monitoring station."""

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._river = river
        self._town = town

        self.latest_level = None

    @property
    def station_id(self):
        return self._station_id

    @property
    def measure_id(self):
        return self._measure_id

    @property
    def name(self):
        return self._name

    @property
    def coord(self):
        return self._coord

    @property
    def typical_range(self):
        return self._typical_range

    @property
    def river(self):
        return self._river

    @property
    def town(self):
        return self._town

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Method that checks the typical high/low range data for consistency.
        Inconsistent is defined as:
            (i) no data is availble
            (ii) reported typical high range is less than the reported typical low range
        Parameters: None
        Returns:
            True if consistent
            False if inconsistent
        """

        if type(self.typical_range) != tuple:
            return False
        elif len(self.typical_range) != 2:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True

    def relative_water_level(self):
        """
        Returns the latest water level as a fraction of the typical range,
        i.e. a ratio of 1.0 corresponds to a level at the typical high
        and a ratio of 0.0 corresponds to a level at the typical low.
        If the necessary data is not available or is inconsistent, the function should return None.
        """

        if self.typical_range_consistent() is True and self.latest_level is not None:
            return (self.latest_level - self.typical_range[0]) / (
                self.typical_range[1] - self.typical_range[0]
            )
        else:
            return None


def inconsistent_typical_range_stations(
    stations: [MonitoringStation],
) -> [MonitoringStation]:
    """Returns a list of all the stations with inconsistent typical ranges
    Parameters:
        stations : [MonitoringStation]
    returns:
        [MonitoringStation]
    """

    return [i for i in stations if not i.typical_range_consistent()]
