import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from modules.sentiment_analysis import analyze_sentiment
from modules.entity_extraction import extract_entities_to_df

def create_visualizations(df):
    # Sentiment Analysis
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    sentiment_histogram = px.histogram(df, x='sentiment', title='Sentiment Distribution')
    sentiment_pie = px.pie(df, names='sentiment', title='Sentiment Pie Chart')

    # Entity Extraction
    entity_df = extract_entities_to_df(df)
    entity_bar = px.bar(entity_df, x='entity_text', color='entity_label',
                         title='Entity Counts by Type',
                         labels={'entity_text': 'Entity', 'entity_label': 'Type'})
    entity_treemap = px.treemap(entity_df, path=['entity_label', 'entity_text'],
                                 title='Entity Treemap')

    # Heatmap (Example: Time-based heatmap of tweets)
    heatmap_data = df[['created_at', 'sentiment']].copy()
    heatmap_data['hour'] = pd.to_datetime(heatmap_data['created_at']).dt.hour
    heatmap = px.density_heatmap(heatmap_data, x='hour', y='sentiment', title='Sentiment Heatmap')

    return {
        'sentiment_histogram': sentiment_histogram,
        'sentiment_pie': sentiment_pie,
        'entity_bar': entity_bar,
        'entity_treemap': entity_treemap,
        'heatmap': heatmap
    }