from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

#H1 is the header for writing
#app.title give the file a name otherwise they name defaultly

app = Dash(__name__)
app.title = "Exercise 3"
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")




image_path = 'assets/Tired_Happy.png'

app.layout = [html.H1('Trulululu'), 
              html.Img(src=image_path),
              dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 'Malaysia', id='dropdown-country'), 
              dcc.Graph(id="grahp-scatter"), 
              dcc.Dropdown([{'label':'2020', 'value': 2020}, {'label':'2010', 'value': 2010}, {'label':'2000', 'value': 2000}], '2000', id='dropdown-year'), 
              dcc.Graph(id="graph-pie")]

@callback(
    Output('graph-scatter','figure'),
    Output('graph-pie','figure'),
    Input('dropdown-country', 'value')
    Input('year', 'value')
)

def update_graph(country_selected, year_selected):
    subset_my = df[df['country'].isin([country_selected])]
    fig = px.scatter(subset_my, x = "year", y = "gdp")

    subset_year = df[df['year'].isin([year_selected])]
    subset_year_Asia = subset_year[subset_year['state'].isin(["Asia"])]
    subset_year_Africa = subset_year[subset_year['state'].isin(["Africa"])]
    subset_year_America = subset_year[subset_year['state'].isin(["America"])]
    subset_year_Europe = subset_year[subset_year['state'].isin(["Europe"])]
    subset_year_Oceania = subset_year[subset_year['state'].isin(["Oceania"])]
    pie_data = [sum(subset_year_Asia['gdp']),sum(subset_year_Africa['gdp']),sum(subset_year_America['gdp']),sum(subset_year_Europe['gdp']),sum(subset_year_Oceania['gdp'])];
    mylabels = ["Asia","Africa","America","Europe","Oceania"]
    pie_df = {'continent': mylabels,'gdp': pie_data}
    fig2 = px.pie(pie_df,values = "gdp", names = "continent")

    return fig

if __name__ == '__main__':
    #dah ok baru remove debug tu
    app.run(debug=True)
