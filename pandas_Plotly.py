import pandas as pd
import plotly.express as px

data = {"country":["Finnland","Denmark"],
      "scoure":[7,6]}
df = pd.DataFrame(data)

# test

fig = px.bar(df, 
             x="country",
             y="scoure",
             title="Hier steht die Überschrift",
             color="scoure")

fig.show()