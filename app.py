"""Script to produce shiny dashboard with markers for each station"""

# Run with ```run shiny```
from ipyleaflet import Map, MarkerCluster, CircleMarker
from shiny.express import ui
from shinywidgets import render_widget
from floodsystem.stationdata import build_station_list

stations = build_station_list()

ui.h2("Map Showing Flood Station Locations")

@render_widget
def map():
    """Function to draw map of all flood stations"""
    map = Map(center=(52.3555, 1.1743), zoom=6, width = 1, height = 3)

    markers = tuple((CircleMarker(location = i.coord, radius = 3, color = "red") for i in stations))

    marker_cluster = MarkerCluster(markers = markers, max_cluser_radius = 10)

    map.add_layer(marker_cluster)

    return map