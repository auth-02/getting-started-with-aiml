from flask import Flask, render_template, request
import pandas as pd
from google_play_scraper import app, Sort, reviews
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
import os
app = Flask(__name__)
sid = SentimentIntensityAnalyzer()
picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder
@app.route('/')
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    return render_template('NEXT.html', user_image=pic1)
@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form.get('input_text')
    app_packages = [input_text]
    result, _ = reviews(
    app_packages[0],
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=1000
    )
    df = pd.json_normalize(result)
    df['content'] = df['content'].astype('str')
    df['sentiment'] = df['content'].apply(lambda x: sid.polarity_scores(x))
    df['sentiment'] = df['sentiment'].apply(lambda x: 'POSITIVE' if x['compound'] >= 0 else 'NEGATIVE')
    fig = px.histogram(df, x='sentiment', color='sentiment', text_auto=True)        
    fig.show()
    pos_count = df['sentiment'].value_counts()['POSITIVE']
    neg_count = df['sentiment'].value_counts()['NEGATIVE']    
    
    if (pos_count > neg_count):
        recommendation ="The app is Safe to download"
    else:
        recommendation ="The app is not Safe to download, Look for an alternative"
    rating =round(df['score'].sum() / len(df), 1)        
    print("recommendation", recommendation)
    print("rating", rating) 
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'bg_result.jpg')
    return render_template('result.html', recommendation=recommendation, rating=rating, user_image=pic2)
if __name__ == '__main__':
    app.run(debug=True)
