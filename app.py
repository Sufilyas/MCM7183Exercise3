from dash import Dash, html, dcc
import numpy as np 
import pandas as pd 
import plotly.express as px

#H1 is the header for writing
#app.title give the file a name otherwise they name defaultly

app = Dash(__name__)
app.title = "Exercise 3"
server = app.server

df = pd.read_csv("https://github.com/Sufilyas/MCM7183Exercise3/blob/main/assets/gdp_1960_2020.csv")
subset_my = df[df['country'].isin(["Malaysia"])]
fig = px.scatter(subset_my, x = "year", y = "gdp")

app.layout = html.H1('Trulululu')

if __name__ == '__main__':
    app.run(debug=True)
