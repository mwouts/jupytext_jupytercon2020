# A quick plot of the Iris dataset using Plotly:

import plotly.express as px

df = px.data.iris()

fig = px.scatter(df,
                 x="sepal_width",
                 y="sepal_length",
                 color="species")

fig.show()
