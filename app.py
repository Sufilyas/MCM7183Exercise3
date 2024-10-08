from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px

#H1 is the header for writing
#app.title give the file a name otherwise they name defaultly

app = Dash(__name__)
app.title = "Assignment 3 Sufina"
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/Sufilyas/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")




image_path = 'assets/Multimedia_University_logo.png'

app.layout = [html.H1('Assignment 3'), 
              html.Img(src=image_path),
              html.Div(id='debug'),
              dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 
                           'Malaysia', id='dropdown-country'), 
              dcc.Graph(id="graph-scatter"), 
              dcc.Dropdown([{'label':'2020', 'value': 2020}, 
                            {'label':'2010', 'value': 2010}, 
                            {'label':'2000', 'value': 2000}], 
                            2020, id='dropdown-year'), 
              dcc.Graph(id="graph-pie")]

@callback(
    Output('graph-scatter','figure'),
    Output('graph-pie','figure'),
    #Output('debug','children'),
    Input('dropdown-country', 'value'),
    Input('dropdown-year', 'value'),
)
def update_graph(country_selected, year_selected):

    # Scatter plot
    subset_Country = df[df['country'].isin([country_selected])]
    fig = px.scatter(subset_Country, x = "year", y = "gdp")

    # Pie Chart
    subset_year = df[df['year'].isin([year_selected])]
    subset_year_Asia = subset_year[subset_year['state'].isin(["Asia"])]
    subset_year_Africa = subset_year[subset_year['state'].isin(["Africa"])]
    subset_year_America = subset_year[subset_year['state'].isin(["America"])]
    subset_year_Europe = subset_year[subset_year['state'].isin(["Europe"])]
    subset_year_Oceania = subset_year[subset_year['state'].isin(["Oceania"])]
    pie_data = [sum(subset_year_Asia['gdp']),
                sum(subset_year_Africa['gdp']),
                sum(subset_year_America['gdp']),
                sum(subset_year_Europe['gdp']),
                sum(subset_year_Oceania['gdp'])];
    mylabels = ["Asia","Africa","America","Europe","Oceania"]
    pie_df = {'Continent': mylabels,'GDP': pie_data}
    fig2 = px.pie(pie_df,values = "GDP", names = "Continent")

    return fig,fig2

if __name__ == '__main__':
    #dah ok baru remove debug tu
    app.run(debug=True)
