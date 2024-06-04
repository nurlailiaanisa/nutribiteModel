import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

# Load the dataset
data = pd.read_csv('resep_new.csv', encoding='unicode_escape')

# Preprocess the data (example: handling missing values, text preprocessing, etc.)
data = data.drop(columns=['sub_title', 'pcnt_cal_prot', 'pcnt_cal_fat', 'pcnt_cal_carb', 'fiber', 'vitamin_c', 'vitamin_a', 'iron', 'sodium', 'cholestrl', 'alcohol', 'source', 'stnd_min', 'sat_fat'], axis=1)
data[['yield_unit', 'intro']] = data[['yield_unit', 'intro']].fillna("NaN")
data[['servings', 'prep_min', 'cook_min']] = data[['servings', 'prep_min', 'cook_min']].fillna(0)

# Calories standar
calories_per_day = 2000
meal_frequency = 3
calories_per_meal = calories_per_day / meal_frequency

# Filter data based on calories
data = data[data['calories'] < calories_per_meal]

# Create TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['directions'])

# Initialize KNN model
n_neighbors = 5
knn = NearestNeighbors(metric='cosine')
knn.fit(tfidf_matrix)

# Save the model and vectorizer to a pickle file
with open('knn_model.pkl', 'wb') as model_file:
    pickle.dump((knn, tfidf_vectorizer), model_file)

print("Model has been trained and saved as 'knn_model.pkl'.")
