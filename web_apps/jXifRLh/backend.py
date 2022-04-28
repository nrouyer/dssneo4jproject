from bokeh.plotting import figure, show, output_file

output_file('image.html')

p = figure(x_range=(0,1), y_range=(0,1))
p.image_url(url=['/local/static/wine_tasting.jpg'], x=0, y=1, w=0.8, h=0.6)
## could also leave out keywords
# p.image_url(['tree.png'], 0, 1, 0.8, h=0.6)  
show(p)
