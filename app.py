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

subset_2020_Asia = subset_2020[subset_2020['state'].isin(["Asia"])]
subset_2020_Africa = subset_2020[subset_2020['state'].isin(["Africa"])]
subset_2020_America = subset_2020[subset_2020['state'].isin(["America"])]
subset_2020_Europe = subset_2020[subset_2020['state'].isin(["Europe"])]
subset_2020_Oceania = subset_2020[subset_2020['state'].isin(["Oceania"])]
pie_data = [sum(subset_2020_Asia['gdp']),sum(subset_2020_Africa['gdp']),sum(subset_2020_America['gdp']),sum(subset_2020_Europe['gdp']),sum(subset_2020_Oceania['gdp'])];
mylabels = ["Asia","Africa","America","Europe","Oceania"]
plt.pie(pie_data, labels = mylabels)
pie_df = {'continent': mylabels,'gdp': pie_data}
fig2 = px.pie(pie_df,values = "gdp", names = "continent")


app.layout = html.H1('Trulululu')

if __name__ == '__main__':
    app.run(debug=True)
