from flask import Flask, render_template
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import os

# Initialize the Flask app
server = Flask(__name__)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

# Define a route for the Flask app
@server.route('/')
def index():
    return render_template('index.html')  # A simple HTML page for the main route

# Initialize the Dash app, and pass the Flask server to Dash
app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')

# Generate some data for the graph
x = np.linspace(0, 10, 100)

# Define the layout for the Dash app
app.layout = html.Div(children=[
    html.H1(children='Dash Plot in Flask'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(x=x, y=np.sin(x), mode='lines', name='Sin(x)')
            ],
            'layout': go.Layout(
                title='Sine Wave',
                xaxis={'title': 'X axis'},
                yaxis={'title': 'Y axis'}
            )
        }
    ),

    # Dropdown to select function type
    dcc.Dropdown(
        id='function-selector',
        options=[
            {'label': 'Sine', 'value': 'sin'},
            {'label': 'Cosine', 'value': 'cos'}
        ],
        value='sin'
    )
])

# Define the callback to update the graph based on dropdown selection
@app.callback(
    Output('example-graph', 'figure'),
    [Input('function-selector', 'value')]
)
def update_graph(selected_function):
    if selected_function == 'sin':
        y = np.sin(x)
    else:
        y = np.cos(x)

    return {
        'data': [
            go.Scatter(x=x, y=y, mode='lines', name=f'{selected_function}(x)')
        ],
        'layout': go.Layout(
            title=f'{selected_function.capitalize()} Wave',
            xaxis={'title': 'X axis'},
            yaxis={'title': 'Y axis'}
        )
    }

# Run the server
if __name__ == '__main__':
    server.run(debug=True, port = 5001)