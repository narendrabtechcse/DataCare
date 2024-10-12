from flask import Flask, render_template
from dashboard import create_dashboard

app = Flask(__name__)

# Create and link the Dash app with the Flask app
dash_app = create_dashboard(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)