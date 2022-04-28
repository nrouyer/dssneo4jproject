from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.plotting import figure
from bokeh.charts import HeatMap, bins, output_file, show, vplot
from bokeh.palettes import RdYlGn6, RdYlGn9
from bokeh.sampledata.autompg import autompg
from bokeh.sampledata.unemployment1948 import data
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

hm = HeatMap(df, x='person1', y='person2',values='score', title='Wine Tasting Similarity', stat=None)
show(hm)

