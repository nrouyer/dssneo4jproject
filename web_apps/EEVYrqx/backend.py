import dataiku
from bokeh.io import curdoc
from bokeh.plotting import figure
import pandas
from pandas import DataFrame


# Uncomment the following to read your own dataset
dataset = dataiku.Dataset("person_taste_matrix")
df = dataset.get_dataframe()
column = "score"




value_counts = df[column].value_counts(bins=8, sort=False)
values = value_counts.index.map(str).values

hist = figure(x_range=values, plot_height=250)
hist.vbar(x=values, top=value_counts, width=0.8)

# For more details about Bokeh's histograms and other charts,
# check Bokeh's documentation:
# https://bokeh.pydata.org

curdoc().add_root(hist)