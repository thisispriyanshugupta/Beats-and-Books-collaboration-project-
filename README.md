# Beats-and-Books Collaboration Project

Welcome to Beats and Books! Seamlessly bridging literary and musical worlds, our app suggests songs based on your favorite books. Dive into '1984' or 'Harry Potter,' our platform provides tailored song recommendations, enhancing your reading experience with curated playlists. Elevate your journey with our intuitive app!

This project implements a recommendation system that suggests songs based on book titles. It uses TF-IDF vectorization and cosine similarity to find similar songs for a given book title.

## Getting Started

To run this project locally, follow these steps:

1. **Clone the Repository:**

    ```
    git clone https://github.com/thisispriyanshugupta/Beats-and-Books-collaboration-project-.git
    ```

2. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

    - Flask
    - pandas
    - scikit-learn
    - fuzzywuzzy
    - autocorrect

3. **Prepare Data:**

    Ensure you have the CSV files `books_dataset_unique.csv` and `songs_dataset_unique.csv` in the project directory. These files contain the dataset of books and songs respectively.

4. **Run the Application:**

    ```
    python app.py
    ```

    The application will run on http://localhost:5000 by default.

## Usage

1. Open your web browser and navigate to http://localhost:5000.
2. Enter a book title in the provided form and specify the number of song recommendations you'd like.
3. Click on the "Get Recommendations" button.
4. The application will display the recommended songs based on the entered book title.

## Project Structure

- `app.py`: Contains the Flask application code including routes and recommendation logic.
- `templates/`: Directory containing HTML templates for rendering pages.
  - `index.html`: Template for the main page with the input form.
  - `recommendations.html`: Template for displaying song recommendations.
  - `error.html`: Template for displaying an error page if the book title is not found.
- `books_dataset_unique.csv`: CSV file containing the dataset of books with their descriptions.
- `songs_dataset_unique.csv`: CSV file containing the dataset of songs with their details.

## Dependencies

- Flask
- pandas
- scikit-learn
- fuzzywuzzy
- autocorrect

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

--- 
