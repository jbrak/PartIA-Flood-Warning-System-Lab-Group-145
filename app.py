"""Script to produce shiny dashboard with markers for each station"""

# Run with ```run shiny```
from ipyleaflet import Map, MarkerCluster, CircleMarker
from shiny.express import ui
from shinywidgets import render_widget
from shiny import render
from shiny.types import ImgData
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

# Build the station list
stations = build_station_list()

# Generate data for graphs
dates = []
levels = []

for station in stations[:6]:
    dt = 5
    date, level = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    dates.append(date)
    levels.append(level)


ui.h2("Map Showing Flood Station Locations")

@render_widget
def map():
    """Function to draw map of all flood stations"""
    map = Map(center=(52.3555, 1.1743), zoom=6, width = 1, height = 3)

    markers = tuple((CircleMarker(location = i.coord, radius = 3, color = "red") for i in stations))

    marker_cluster = MarkerCluster(markers = markers, max_cluser_radius = 10)

    map.add_layer(marker_cluster)

    return map

ui.h2("Graphs showing water level against time for different stations")

@render.image()
def graph():
    """ Function to plot the graphs of the water levels as an image """

    plot_water_level_with_fit(stations[:6], dates, levels,p=4, img = "cache/img.png")

    img: ImgData = {"src": "cache/img.png", "width" : "100%"}
    return img
