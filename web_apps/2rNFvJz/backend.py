from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.plotting import figure
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

x = df[x_column]
y = df[y_column]
source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(plot_height=400, plot_width=400, title=y_column+" by "+x_column,
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[min(x), max(x)], y_range=[min(y),max(y)])

plot.scatter('x', 'y', source=source)

# Set up layouts and add to document
inputs = widgetbox()

curdoc().add_root(row(inputs, plot, width=800))
