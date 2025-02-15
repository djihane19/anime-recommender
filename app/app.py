from flask import Flask, request, render_template  
import pandas as pd  
import pickle  
from fuzzywuzzy import process  # Import fuzzy matching  

# Load data & precomputed similarity matrix  
anime_df = pd.read_csv("../data/anime_cleaned.csv")  # Ensure this file exists  

with open("../models/cosine_sim.pkl", "rb") as f:  
    cosine_sim = pickle.load(f)  

with open("../models/indices.pkl", "rb") as f:  
    indices = pickle.load(f)  

# Convert anime titles to lowercase for case-insensitive matching  
anime_df["name_lower"] = anime_df["name"].str.lower()  
indices = {title.lower(): i for title, i in indices.items()}  

app = Flask(__name__)  

# Recommendation function with fuzzy matching  
def get_recommendations(title):  
    title = title.lower().strip()  

    # Find the best match  
    best_match, score = process.extractOne(title, indices.keys())  
    if score < 60:  # If no good match, return nothing  
        return [], None  

    idx = indices[best_match]  
    sim_scores = sorted(enumerate(cosine_sim[idx]), key=lambda x: x[1], reverse=True)[1:11]  
    anime_indices = [i[0] for i in sim_scores]  

    return anime_df["name"].iloc[anime_indices].tolist(), best_match  

@app.route("/", methods=["GET", "POST"])  
def home():  
    recommendations = []  
    search_query = ""  
    best_match = ""  

    if request.method == "POST":  
        search_query = request.form["anime_title"]  
        recommendations, best_match = get_recommendations(search_query)  

    return render_template("index.html", query=search_query, best_match=best_match, recommendations=recommendations)  

if __name__ == "__main__":  
    app.run(debug=True)  
