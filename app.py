from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 

app = Flask(__name__)

# Load data and pre-process
books_df = pd.read_csv('books_dataset_unique.csv')
songs_df = pd.read_csv('songs_dataset_unique.csv')
merged_df = pd.merge(books_df, songs_df, left_on='Book_ID', right_on='Song_ID')
df = pd.DataFrame(merged_df)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommendation function
def get_song_recommendations(book_title, n=3, cosine_sim=cosine_sim):
    idx = df.index[df['Title'] == book_title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]  # Get the top n most similar songs

    song_indices = [i[0] for i in sim_scores]
    return df['Song Name'].iloc[song_indices]

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    book_title = request.form['book_title']
    num_recommendations = int(request.form['num_recommendations'])
    recommendations = get_song_recommendations(book_title, num_recommendations)
    return render_template('recommendations.html', book_title=book_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
