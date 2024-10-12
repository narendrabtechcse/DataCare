import spacy
import pandas as pd


nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]


def extract_entities_to_df(df):
    entity_rows = []
    for text in df['text']:
        entities = extract_entities(text)
        for entity in entities:
            entity_rows.append({'entity_text': entity[0], 'entity_label': entity[1]})

    return pd.DataFrame(entity_rows)