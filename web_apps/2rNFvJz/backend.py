from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.plotting import figure
import dataiku
import pandas as pd

# Parameterize webapp inputs
input_dataset = "Orders_enriched_prepared"
x_column = "age"
y_column = "total"
time_column = "order_date_year"
cat_column = "tshirt_category"

