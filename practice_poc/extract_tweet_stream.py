import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Step 1: Load your text dataset
# For demonstration, we'll create a sample DataFrame. Replace this with your actual data loading method.
data = {
    'Text': [
        "I love programming in Python! It's so versatile.",
        "The weather is terrible today.",
        "I'm feeling great about my project.",
        "This is the worst experience I've ever had.",
        "I'm not sure how I feel about this."
    ]
}

df = pd.DataFrame(data)

# Step 2: Initialize the Sentiment Intensity Analyzer
# nltk.download('vader_lexicon')  # Ensure the VADER lexicon is downloaded
sid = SentimentIntensityAnalyzer()

# Step 3: Define a function to get sentiment scores
def get_sentiment(text):
    scores = sid.polarity_scores(text)
    return scores['compound'], scores['pos'], scores['neu'], scores['neg']

# Step 4: Apply the function to the DataFrame
df[['Compound Score', 'Positive Score', 'Neutral Score', 'Negative Score']] = df['Text'].apply(get_sentiment).apply(pd.Series)

# Step 5: Initialize RAKE for keyword extraction
rake = Rake()

# Step 6: Define a function to extract keywords
def extract_keywords(text):
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()

# Step 7: Apply the function to extract keywords
df['Keywords'] = df['Text'].apply(extract_keywords)

# Step 8: Display the DataFrame with sentiment insights and keywords
print(df.columns)

# Optional: Analyze overall sentiment distribution
overall_sentiment = df[['Compound Score']].describe()
print("\nOverall Sentiment Distribution:\n", overall_sentiment)