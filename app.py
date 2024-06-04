from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer from the pickle file
with open('knn_model.pkl', 'rb') as model_file:
    knn, tfidf_vectorizer = pickle.load(model_file)

# Load the original dataset
data = pd.read_csv('resep_new.csv', encoding='unicode_escape')

# Preprocess the data in the same way as during training
data = data.drop(columns=['sub_title', 'pcnt_cal_prot', 'pcnt_cal_fat', 'pcnt_cal_carb', 'fiber', 'vitamin_c', 'vitamin_a', 'iron', 'sodium', 'cholestrl', 'alcohol', 'source', 'stnd_min', 'sat_fat'], axis=1)
data[['yield_unit', 'intro']] = data[['yield_unit', 'intro']].fillna("NaN")
data[['servings', 'prep_min', 'cook_min']] = data[['servings', 'prep_min', 'cook_min']].fillna(0)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    try:
        liked_data = pd.read_csv(file, encoding='unicode_escape')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    if 'directions' not in liked_data.columns:
        return jsonify({'error': 'CSV file must contain a "directions" column'}), 400

    liked_recipe_vector = tfidf_vectorizer.transform(liked_data['directions'])

    # Find similar recipes
    n_neighbors = 5
    distances, indices = knn.kneighbors(liked_recipe_vector, n_neighbors=n_neighbors)

    # If the number of recommendations is less than 5, increase n_neighbors
    while indices.shape[1] < 5:
        n_neighbors += 1
        distances, indices = knn.kneighbors(liked_recipe_vector, n_neighbors=n_neighbors)

    # Get the top 5 recommendations for each liked recipe
    all_recommendations = []
    for i in range(len(liked_data)):
        recommended_meals = data.iloc[indices[i, :5]].to_dict(orient='records')
        all_recommendations.append(recommended_meals)

    return jsonify(all_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
