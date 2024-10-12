import pandas as pd
import json


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    df = pd.json_normalize(data)
    df = cleanse_data(df)
    return df


def cleanse_data(df):
    df = df.dropna(subset=['text'])  # Remove rows with missing tweet text
    df['text'] = df['text'].str.lower()  # Convert text to lowercase
    return df

