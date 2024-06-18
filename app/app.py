from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the dataset
dataset = pd.read_csv('resep_new.csv', encoding='unicode_escape')

# Preprocess the data
columns_to_drop = [
    'sub_title', 'pcnt_cal_prot', 'pcnt_cal_fat', 'pcnt_cal_carb', 'fiber', 
    'vitamin_c', 'vitamin_a', 'iron', 'sodium', 'cholestrl', 'alcohol', 
    'source', 'stnd_min', 'sat_fat'
]
dataset = dataset.drop(columns=columns_to_drop, axis=1)
dataset[['yield_unit', 'intro']] = dataset[['yield_unit', 'intro']].fillna("NaN")
dataset[['servings', 'prep_min', 'cook_min']] = dataset[['servings', 'prep_min', 'cook_min']].fillna(0)

# Create the TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['directions'])

# Create the KNN model
knn = NearestNeighbors(metric='cosine')
knn.fit(tfidf_matrix)

@app.route('/')
def home():
    return "Welcome to Recipe Recommendation System"

@app.route('/predict', methods=['POST'])
def recommend_recipes():
    data = request.get_json()

    if 'calories' not in data:
        return jsonify({'error': 'Calories information is required'}), 400

    try:
        calories_per_day = int(data['calories'])
    except ValueError:
        return jsonify({'error': 'Invalid calories value'}), 400

    meal_frequency = 3
    calories_per_meal = calories_per_day / meal_frequency

    # Filter dataset based on calories
    data_filtered = dataset[dataset['calories'] < calories_per_meal]

    if 'liked_recipes' not in data or not data['liked_recipes']:
        # Return all recipes if no liked recipes are provided or liked_recipes is an empty list
        return jsonify(data_filtered.to_dict(orient='records'))

    liked_recipes_data = pd.DataFrame(data['liked_recipes'])

    if 'directions' not in liked_recipes_data.columns:
        return jsonify({'error': 'Liked recipes data must contain a "directions" column'}), 400

    # Transform liked recipe directions
    liked_recipe_vector = tfidf_vectorizer.transform(liked_recipes_data['directions'])

    # Find similar recipes
    n_neighbors = 20
    min_recommendations = 5
    distances, indices = knn.kneighbors(liked_recipe_vector, n_neighbors=n_neighbors)

    # Ensure the number of recommendations does not exceed available recipes
    if indices.shape[1] < min_recommendations:
        min_recommendations = indices.shape[1]

    # Get the top recommendations for each liked recipe
    all_recommendations = []
    for i in range(len(liked_recipes_data)):
        recommended_indices = indices[i, :min_recommendations]
        valid_indices = recommended_indices[recommended_indices < len(data_filtered)]
        recommended_meals = data_filtered.iloc[valid_indices].to_dict(orient='records')
        all_recommendations.append(recommended_meals)

    return jsonify(all_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
