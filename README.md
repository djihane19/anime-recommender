# 🎌 Anime Recommender System

A **content-based recommendation system** built with **Flask** and **cosine similarity**, enhanced by **fuzzy search** for better title matching.  
This project recommends anime similar to a user’s input using **precomputed embeddings** and displays results in a clean web interface.

---

## 🚀 Features

- 🔍 Fuzzy matching for anime title inputs
- 📈 Content-based similarity using cosine similarity
- 🧠 Precomputed similarity matrix for fast recommendations
- 🖥️ Clean Flask-based web interface
- 📂 Modular folder structure (models, data, templates)

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **ML/Similarity**: cosine similarity, pickle
- **Libraries**: pandas, fuzzywuzzy, scikit-learn
- **Frontend**: HTML, CSS (custom styling)
- **Data**: Cleaned anime dataset (`anime_cleaned.csv`)

---

## 🧠 How It Works

1. The app loads a cleaned anime dataset and a precomputed cosine similarity matrix.
2. When a user inputs an anime name:
   - Fuzzy string matching finds the closest match from the dataset.
   - The system fetches the most similar anime titles using cosine similarity scores.
3. The top 10 similar anime are returned and displayed in a simple interface.

---



