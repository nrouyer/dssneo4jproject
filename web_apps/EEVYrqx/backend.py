import dataiku
from bokeh.io import curdoc
from bokeh.plotting import figure
import pandas
from pandas import DataFrame


# Uncomment the following to read your own dataset
dataset = dataiku.Dataset("person_taste_matrix")
df = dataset.get_dataframe()
column = "score"

source = ColumnDataSource(df)

# this is the colormap from the original NYTimes plot
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
mapper = LinearColorMapper(palette=colors, low=df.score.min(), high=df.score.max())

p = figure(width=800, height=300, title="US unemployment 1948—2016",
           x_range=list(df.person1), y_range=list(df.person2),
           toolbar_location=None, tools="", x_axis_location="above")

p.rect(x="Person1", y="Person2", width=1, height=1, source=source,
       line_color=None, fill_color=transform('score', mapper))

color_bar = ColorBar(color_mapper=mapper,
                     ticker=BasicTicker(desired_num_ticks=len(colors)),
                     formatter=PrintfTickFormatter(format="%d%%"))

p.add_layout(color_bar, 'right')

p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "7px"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = 1.0

value_counts = df[column].value_counts(bins=8, sort=False)
values = value_counts.index.map(str).values

hist = figure(x_range=values, plot_height=250)
hist.vbar(x=values, top=value_counts, width=0.8)

# For more details about Bokeh's histograms and other charts,
# check Bokeh's documentation:
# https://bokeh.pydata.org

curdoc().add_root(p)