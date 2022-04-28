from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.plotting import figure
import numpy as np
import holoviews as hv
from holoviews import streams
hv.extension('bokeh', width=90)
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


