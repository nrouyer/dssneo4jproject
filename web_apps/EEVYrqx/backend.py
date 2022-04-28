import dataiku
from bokeh.io import curdoc, output_file, show
from bokeh.plotting import figure
import pandas
from pandas import DataFrame
from bokeh.models import (BasicTicker, ColorBar, ColumnDataSource,
                          LinearColorMapper, PrintfTickFormatter)
from bokeh.transform import transform

# Uncomment the following to read your own dataset
dataset = dataiku.Dataset("person_taste_matrix")
df = dataset.get_dataframe()
column = "score"

from bokeh.plotting import figure, show

colors = ['#2765a3' for x in range(20)]
x = list(range(10)) * 2
y = ['a'] * 10 +  ['b'] * 10

hm = figure(y_range=('a', 'b'))
hm.rect(x, y, width=1, height=1, fill_color=colors, line_color="white")

show(hm)

curdoc().add_root(hm)