from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 
from fuzzywuzzy import fuzz 
from autocorrect import Speller # Import fuzzywuzzy library


app = Flask(__name__)


# Load data and pre-process
books_df = pd.read_csv('books_dataset_unique.csv')
songs_df = pd.read_csv('songs_dataset_unique.csv')
merged_df = pd.merge(books_df, songs_df, left_on='Book_ID', right_on='Song_ID')
df = pd.DataFrame(merged_df)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Initialize autocorrect spell checker
spell = Speller()

# Recommendation function
def get_song_recommendations(book_title, n=3, cosine_sim=cosine_sim):
    # Convert book_title to lowercase
    book_title = book_title.lower()

    # Spell check and auto-correct
    book_title_corrected = spell(book_title)

    try:
        # Check if corrected book title exists in the database
        idx = df.index[df['Title'].str.lower() == book_title_corrected].tolist()[0]
    except IndexError:
        return None  # Return None if book title not found
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]  # Get the top n most similar songs

    song_indices = [i[0] for i in sim_scores]
    return df['Song Name'].iloc[song_indices]

# Extract book titles from the DataFrame
books = books_df['Title'].tolist()

# Flask routes

@app.route('/')
def index():
    return render_template('final.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search_term = request.args.get('term')
    if search_term:
        # Filter books by partial match with search term
        suggestions = [book for book in books if search_term.lower() in book.lower()]
        # Limit suggestions to top 5
        suggestions = suggestions[:5]
        return jsonify(suggestions)
    return jsonify([])


@app.route('/recommendations', methods=['POST'])
def recommendations():
    book_title = request.form['book_title']
    num_recommendations = int(request.form['num_recommendations'])
    recommendations = get_song_recommendations(book_title, num_recommendations)
    if recommendations is None:
        return render_template('error.html')  # Render error page if book title not found
    return render_template('recommendations.html', book_title=book_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)

