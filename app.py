from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

content_data = pd.read_csv('data/content.csv')

def recommend_content(user_interest):

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(content_data['description'])
    
    user_vec = tfidf.transform([user_interest])
    cosine_sim = cosine_similarity(user_vec, tfidf_matrix)
    
    similar_indices = cosine_sim[0].argsort()[-5:][::-1]
    recommendations = content_data.iloc[similar_indices]
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_interest = request.form['interest']
    recommendations = recommend_content(user_interest)
    return render_template('recommendations.html', content_list=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
