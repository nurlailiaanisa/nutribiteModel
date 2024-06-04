import pandas as pd
import pickle

# Load the model and vectorizer from the pickle file
with open('knn_model.pkl', 'rb') as model_file:
    knn, tfidf_vectorizer = pickle.load(model_file)

# Load the original dataset
data = pd.read_csv('resep_new.csv', encoding='unicode_escape')

# Preprocess the data in the same way as during training
data = data.drop(columns=['sub_title', 'pcnt_cal_prot', 'pcnt_cal_fat', 'pcnt_cal_carb', 'fiber', 'vitamin_c', 'vitamin_a', 'iron', 'sodium', 'cholestrl', 'alcohol', 'source', 'stnd_min', 'sat_fat'], axis=1)
data[['yield_unit', 'intro']] = data[['yield_unit', 'intro']].fillna("NaN")
data[['servings', 'prep_min', 'cook_min']] = data[['servings', 'prep_min', 'cook_min']].fillna(0)

# Load the liked recipes data
liked_data = pd.read_csv('resep_suka_fix.csv', encoding='unicode_escape')
liked_recipe_vector = tfidf_vectorizer.transform(liked_data['directions'])

# Find similar recipes
distances, indices = knn.kneighbors(liked_recipe_vector, n_neighbors=5)

# If the number of recommendations is less than 5, increase n_neighbors
while indices.shape[1] < 5:
    n_neighbors += 1
    distances, indices = knn.kneighbors(liked_recipe_vector, n_neighbors=n_neighbors)

# Get the top 5 recommendations
recommended_meals = data.iloc[indices[0, :5]]

print("Resep yang mirip dengan yang disukai user:")
print(recommended_meals)