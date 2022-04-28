from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput, Select
from bokeh.plotting import figure
from graphdatascience import GraphDataScience
import dataiku
import pandas as pd
import seaborn as sns

# Parameterize webapp inputs
input_dataset = "Orders_enriched_prepared"
x_column = "age"
y_column = "total"
time_column = "order_date_year"
cat_column = "tshirt_category"

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