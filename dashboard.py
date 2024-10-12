import dash
from dash import html, dcc
from modules.data_loader import load_data
from modules.visualization import create_visualizations

def create_dashboard(flask_app):
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        url_base_pathname='/dashboard/'
    )

    df = load_data('data/sample_data.json')
    figures = create_visualizations(df)

    dash_app.layout = html.Div([
        html.H1('Twitter Sentiment Analysis Dashboard'),
        dcc.Tabs([
            dcc.Tab(label='Sentiment Analysis', children=[
                dcc.Graph(figure=figures['sentiment_histogram']),
                dcc.Graph(figure=figures['sentiment_pie']),
            ]),
            dcc.Tab(label='Entity Analysis', children=[
                dcc.Graph(figure=figures['entity_bar']),
                dcc.Graph(figure=figures['entity_treemap']),
            ]),
            dcc.Tab(label='Heatmap', children=[
                dcc.Graph(figure=figures['heatmap']),
            ])
        ])
    ])

    return dash_app