from math import pi
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, PrintfTickFormatter
from bokeh.models.widgets import Slider, TextInput, Select
import numpy as np
from bokeh.plotting import figure, show
import dataiku
import pandas as pd

# Parameterize webapp inputs
input_dataset = "person_taste_matrix"
x_column = "person1"
y_column = "person2"
score_column = "score"

# Set up data
mydataset = dataiku.Dataset(input_dataset)
df = mydataset.get_dataframe()

# this is the colormap from the original NYTimes plot
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
mapper = LinearColorMapper(palette=colors, low=df.rate.min(), high=df.rate.max())

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

p = figure(title="Wine tasting similarity heatmap",
           x_range=person1, y_range=person2,
           x_axis_location="above", width=900, height=400,
           tools=TOOLS, toolbar_location='below')

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "7px"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(x="Person1", y="Person2", width=1, height=1,
       source=df,
       fill_color={'field': 'score', 'transform': mapper},
       line_color=None)

color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="7px",
                     ticker=BasicTicker(desired_num_ticks=len(colors)),
                     formatter=PrintfTickFormatter(format="%d%%"),
                     label_standoff=6, border_line_color=None)
p.add_layout(color_bar, 'right')

show(p)