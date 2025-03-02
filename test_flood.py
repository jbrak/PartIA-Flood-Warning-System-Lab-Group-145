"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


def test_stations_level_over_threshold():
    """Test for the stations_level_over_threshold method"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    trange2 = ()
    trange3 = (3.4445, -2.3)
    trange4 = None
    river = "River X"
    town = "My Town"

    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange4, river, town)
    s1.latest_level = s2.latest_level = s3.latest_level = s4.latest_level = 0
    test_stations = [s1, s2, s3, s4]
    test_stations = stations_level_over_threshold(test_stations, 0.3)
    assert test_stations == [(s1, (0 - -2.3) / (3.4445 - -2.3))]


def test_stations_highest_rel_level():
    """Test for the stations_level_over_threshold method"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    trange2 = ()
    trange3 = (3.4445, -2.3)
    trange4 = None
    river = "River X"
    town = "My Town"

    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange4, river, town)
    s1.latest_level = s2.latest_level = s3.latest_level = s4.latest_level = 0
    test_stations = [s1, s2, s3, s4]
    test_stations = stations_highest_rel_level(test_stations, 1)
    assert test_stations == [s1]
