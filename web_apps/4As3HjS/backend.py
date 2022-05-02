import dataiku
from bokeh.io import curdoc, output_file, show
import pandas as pd
from bokeh.models import (BasicTicker, ColorBar, ColumnDataSource,
                          LinearColorMapper, PrintfTickFormatter)
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.sampledata.unemployment1948 import data
from bokeh.transform import transform

output_file("webapp_wine_tasting.html")

data.Year = data.Year.astype(str)
data = data.set_index('Year')
data.drop('Annual', axis=1, inplace=True)
data.columns.name = 'Month'

# reshape to 1D array or rates with a month and year for each row.
df = pd.DataFrame(data.stack(), columns=['rate']).reset_index()

source = ColumnDataSource(df)

# this is the colormap from the original NYTimes plot
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
mapper = LinearColorMapper(palette=colors, low=df.rate.min(), high=df.rate.max())

p = figure(width=800, height=300, title="US unemployment 1948—2016",
           x_range=list(data.index), y_range=list(reversed(data.columns)),
           toolbar_location=None, tools="", x_axis_location="above")

p.rect(x="Year", y="Month", width=1, height=1, source=source,
       line_color=None, fill_color=transform('rate', mapper))

color_bar = ColorBar(color_mapper=mapper,
                     ticker=BasicTicker(desired_num_ticks=len(colors)),
                     formatter=PrintfTickFormatter(format="%d%%"))

p.add_layout(color_bar, 'right')

p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "7px"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = 1.0

input_dataset = "person_taste_matrix"
x_column = "person1"
y_column = "person2"
score_column = "score"

# Set up data
mydataset = dataiku.Dataset(input_dataset)
df1 = mydataset.get_dataframe()
source1 = ColumnDataSource(df1)

# this is the colormap from the original NYTimes plot
colors1 = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
mapper1 = LinearColorMapper(palette=colors, low=df1.score.min(), high=df1.score.max())

p1 = figure(width=600, height=600, title="Wine tasting similarity",
           x_range=df1['person1'].unique(), y_range=df1['person2'].unique(),
           toolbar_location=None, tools="", x_axis_location="above")

p1.rect(x="person1", y="person2", width=1, height=1, source=source1,
       line_color=None, fill_color=transform('score', mapper1))

#color_bar1 = ColorBar(color_mapper=mapper1,
#                     ticker=BasicTicker(desired_num_ticks=len(colors)),
#                     formatter=PrintfTickFormatter(format="%d%%"))

color_bar1 = ColorBar(color_mapper=mapper1,
                     ticker=BasicTicker(desired_num_ticks=20),
                     formatter=PrintfTickFormatter(format="%.2f"))


p1.add_layout(color_bar1, 'right')

p1.axis.axis_line_color = None
p1.axis.major_tick_line_color = None
p1.axis.major_label_text_font_size = "16px"
p1.axis.major_label_standoff = 0
p1.xaxis.major_label_orientation = 1.0

# Set up widgets
min_score = Slider(title="Minimum score", value=df1.score.min(), start=df1.score.min(), end=df1.score.max(), step=0.05)
max_score = Slider(title="Maximum score", value=df1.score.max(), start=df1.score.min(), end=df1.score.max(), step=0.05)

#Set up update functions and callbacks
def update_data(attrname, old, new):
    selected = df1[(df1.score>=min_score.value) & (df1.score<=max_score.value)]
    # Generate the new plot
    #x = selected[person1]
    #y = selected[person2]
    #source1.data = dict(x=x, y=y, score=score)
    source1 = ColumnDataSource(selected)


for w in [min_score, max_score]:
    w.on_change('value', update_data)    

    
inputs = column(min_score, max_score)
    
#curdoc().add_root(p1)
#curdoc().add_root(min_score)
#curdoc().add_root(max_score)
curdoc().add_root(row(inputs, p1, width=800))

