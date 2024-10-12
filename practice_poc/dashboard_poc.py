import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import numpy as np
import base64


class DataGenerator:
    """Class to generate test data for the application."""

    @staticmethod
    def generate_test_data():
        """Generate a sample DataFrame with tweet data."""
        data = {
            "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
            "tweet": [
                "I love sunny days!",
                "I hate traffic.",
                "Today is a great day!",
                "I'm feeling sad.",
                "What a beautiful morning!",
                "I am frustrated with the weather.",
                "Life is good.",
                "So tired of this!",
                "I'm happy with my job.",
                "I dislike long waits."
            ],
            "tweet_sentiment": np.random.uniform(-1, 1, 10),
            "twitter_sentiment_pattern": [str(np.random.rand(10).tolist()) for _ in range(10)],
            "rcsa": np.random.choice(['A', 'B', 'C'], 10)
        }
        return pd.DataFrame(data)  # Return as a DataFrame


class WordCloudGenerator:
    """Class to generate word cloud images."""

    @staticmethod
    def create_placeholder_wordcloud():
        """Generate a placeholder word cloud image."""
        return base64.b64encode(np.random.rand(100, 100)).decode('utf-8')


class Visualizations:
    """Class to create visualizations using Plotly."""

    def __init__(self, df):
        self.df = df

    def create_heatmap(self):
        """Create a heatmap figure."""
        employees = self.df['name'].tolist()
        data_heatmap = self.df['twitter_sentiment_pattern'].apply(eval).tolist()
        fig = px.imshow(
            np.random.rand(10, 10),
            color_continuous_scale=px.colors.sequential.Emrld,
            title="10 Tweet Sentiment Pattern",
            labels=dict(x="Tweet index", y="Names"),
            x=[str(i) for i in range(1, 11)],
            y=employees
        )
        fig.update_xaxes(side="top")
        fig.update_layout(height=800, width=800)
        return fig

    def create_pie_chart(self):
        """Create a pie chart figure."""
        self.df["sentiment_binary"] = self.df["tweet_sentiment"].apply(lambda x: "negative" if x < 0 else "positive")
        day_sentiment_counts = self.df['sentiment_binary'].value_counts()
        fig = px.pie(
            names=day_sentiment_counts.index,
            values=day_sentiment_counts.values,
            color=day_sentiment_counts.index,
            hole=0.5
        )
        fig.update_traces(textinfo="label + percent", insidetextfont=dict(color="white"))
        fig.update_layout(legend={"itemclick": False})
        return fig

    def create_bar_chart(self, sentiment='overall'):
        """Create a bar chart based on sentiment type."""
        if sentiment == 'positive':
            df_filtered = self.df[self.df['tweet_sentiment'] > 0]
        elif sentiment == 'negative':
            df_filtered = self.df[self.df['tweet_sentiment'] < 0]
        else:
            df_filtered = self.df

        fig = px.bar(
            df_filtered,
            x='name',
            y='tweet_sentiment',
            text='tweet_sentiment',
            color_discrete_sequence=['#00FF00' if sentiment == 'positive' else '#FF0000']
        )
        return fig


class DashApp:
    """Class to create and run the Dash application."""

    def __init__(self, df):
        self.df = df
        self.app = dash.Dash(__name__)
        self.visualizations = Visualizations(df)


    def layout(self):
        """Define the layout of the Dash app."""
        return html.Div([
            html.Img(src="../static/logo.jpg"),
            html.Div(style={"font-family": 'Open Sans', 'background': '#'}, children=[
                # Section for overall tweet sentiment bar graph
                html.Div([
                    html.H1("Sentiments of the Tweets Today"),
                    dcc.Graph(id='graph1', figure=self.visualizations.create_bar_chart())
                ]),
                # Section for overall sentiments pie chart
                html.Div([
                    html.H1("Today's Overall Sentiments"),
                    dcc.Graph(id='graph2', figure=self.visualizations.create_pie_chart())
                ]),
                # Section for significant words in overall tweets (word cloud)
                html.Div([
                    html.H1("Significant Words Used in Overall Tweets"),
                    html.Img(src="data:image/png;base64," + WordCloudGenerator.create_placeholder_wordcloud(),
                             style={'height': '50%', 'width': '50%'})
                ]),
                # Section for heatmap of Twitter users vs sentiment
                html.Div([
                    html.H1("Heatmap of Twitter Users vs Type of Sentiment"),
                    dcc.Graph(id='graph3', figure=self.visualizations.create_heatmap())
                ]),
                # Section for pattern of positive tweets bar graph
                html.Div([
                    html.H1("Pattern of Positive Tweets"),
                    dcc.Graph(id='graph5', figure=self.visualizations.create_bar_chart(sentiment='positive'))
                ]),
                # Section for negative tweet sentiment bar graph
                html.Div([
                    html.H1("Negative Tweet Sentiment"),
                    dcc.Graph(id='graph4', figure=self.visualizations.create_bar_chart(sentiment='negative'))
                ]),
                # Section for overall summary of tweets in a table
                html.Div([
                    html.H1("Overall Summary of Tweets"),
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in self.df.columns],
                        data=self.df.to_dict('records'),
                        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                        style_cell={
                            'whiteSpace': 'normal',
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': 'white'
                        },
                    )
                ])
            ])
        ])


    def run(self):
        """Run the Dash app."""
        self.app.layout = self.layout()
        self.app.run_server(debug=True)


# Main execution
if __name__ == '__main__':
    df = DataGenerator.generate_test_data()  # Generate test data
    app = DashApp(df)  # Initialize the Dash app with the test data
    app.run()  # Run the app