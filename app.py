from dash import Dash, html

app = Dash(__name__)
server = app.server

#H1 is header for writing

app.layout = html.H1('Trulululu')

if __name__ == '__main__':
    app.run(debug=True)
