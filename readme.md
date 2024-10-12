

To download spacy module: 
python -m spacy download en_core_web_sm


# Twitter Sentiment Analysis Dashboard

## Overview
This project is a Flask web application integrated with Plotly Dash to visualize sentiment analysis and entity extraction from Twitter data.

## Features
- **Sentiment Analysis**: Displays sentiment polarity using pie charts and histograms.
- **Entity Extraction**: Shows entity information in bar charts and treemaps.
- **Heatmap Visualization**: Time-based sentiment heatmap.

## How to Run Locally
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/TwitterSentimentDashboard.git
   cd TwitterSentimentDashboard
   
2. Install Dependencies 
pip install -r requirements.txt



## Deployment to AWS EC2

1. Launch an EC2 instance and allow HTTP and SSH traffic.
2. Install necessary software on the server (Python, pip, etc.).
3. Transfer the project files to the server.
4. Set up a virtual environment and install dependencies.
5. Configure Nginx as a reverse proxy for the Flask app.
6. Start the Flask app using gunicorn.


