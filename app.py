from dash import Dash, html, dcc
import numpy as np 
import pandas as pd 
import plotly.express as px

#H1 is the header for writing
#app.title give the file a name otherwise they name defaultly

app = Dash(__name__)
app.title = "Exercise 3"
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")
subset_my = df[df['country'].isin(["Malaysia"])]
fig = px.scatter(subset_my, x = "year", y = "gdp")

subset_year = df[df['year'].isin([2020])]
subset_year_Asia = subset_year[subset_year['state'].isin(["Asia"])]
subset_year_Africa = subset_year[subset_year['state'].isin(["Africa"])]
subset_year_America = subset_year[subset_year['state'].isin(["America"])]
subset_year_Europe = subset_year[subset_year['state'].isin(["Europe"])]
subset_year_Oceania = subset_year[subset_year['state'].isin(["Oceania"])]
pie_data = [sum(subset_year_Asia['gdp']),sum(subset_year_Africa['gdp']),sum(subset_year_America['gdp']),sum(subset_year_Europe['gdp']),sum(subset_year_Oceania['gdp'])];
mylabels = ["Asia","Africa","America","Europe","Oceania"]
pie_df = {'continent': mylabels,'gdp': pie_data}
fig2 = px.pie(pie_df,values = "gdp", names = "continent")

image_path = 'assets/Tired_Happy.png'

app.layout = [html.H1('Trulululu'), html.Img(src=image_path), dcc.Graph(figure=fig), dcc.Graph(figure=fig2)]

if __name__ == '__main__':
    #dah ok baru remove debug tu
    app.run(debug=True)
