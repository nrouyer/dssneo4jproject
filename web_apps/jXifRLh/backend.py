from bokeh.io import curdoc
from bokeh.plotting import figure, show, output_file

output_file('image.html')
path = "/local/static/wine_tasting.jpg"
p = figure(x_range=(0, 1), y_range=(0, 1))
p.image_url(url=[path], x=0, y=1, w=0.8, h=0.6)

show(p)

