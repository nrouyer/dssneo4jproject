''' An interactivate categorized chart based on the wine dataset.
This example shows the ability of Bokeh to create a dashboard with different
sorting options based on a given dataset.

'''
import numpy as np
import pandas

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.plotting import figure
from graphdatascience import GraphDataScience

# Configures the driver with AuraDS-recommended settings
gds = GraphDataScience(
    "neo4j+ssc://35.181.44.209:7687",
    auth=("neo4j", "neo4jdss")
)

# Sets database (if not default one)
gds.set_database("wine")

# get the data from neo4j database
# get similarity matrix data frame from graph
pd = gds.run_cypher(
  """
  MATCH (p1:Person)
  MATCH (p2:Person)
  OPTIONAL MATCH (p1)-[s:SIMILAR]->(p2)
  RETURN p1.name AS person1, p2.name AS person2, coalesce(s.score, 0) AS score
  """
)

sns.heatmap(pd.pivot('person1', 'person2', values='score'), annot=True, cmap="YlGnBu")
# Create Slider object
slider = Slider(start=0, end=1, value=0.5,
                step=0.1, title='Similarity score')

curdoc().add_root(l)
curdoc().title = "Wine taste similarity matrix"