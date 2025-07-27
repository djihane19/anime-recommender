# 🎌 Anime Recommender System (Content-Based + Fuzzy Matching)

This is a **content-based anime recommendation engine** using **cosine similarity** of TF-IDF genre vectors.  
It features a simple **Flask web interface** with fuzzy matching to handle imperfect user input, providing fast and relevant anime suggestions.

---

## 📚 Dataset

The data is sourced from the Kaggle dataset:  
📦 [MyAnimeList Dataset (anime.csv & rating.csv)](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

We cleaned and preprocessed this data to handle:
- Missing genres and ratings
- Normalization of genre data for ML
- Tokenization of multi-genre entries for vectorization

---

## 🔧 Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: TF-IDF, Cosine Similarity
- **Similarity Matching**: `sklearn`, `fuzzywuzzy`, `difflib`
- **Frontend**: HTML + CSS (inline styling)
- **Data Handling**: pandas, pickle
- **Visualization (in notebooks)**: matplotlib, seaborn

---

## 🧠 How It Works

1. **Preprocessing**:
   - Cleans genre strings (e.g., `"Action, Adventure"` → list)
   - Applies TF-IDF vectorization on genres
   - Computes **cosine similarity matrix**
   - Saves similarity matrix and index mapping with `pickle`

2. **Web App**:
   - User enters an anime name (e.g., *"Naruto"*)
   - App uses **fuzzy matching** to find the closest real title
   - Retrieves the top 10 similar anime titles using cosine similarity
   - Displays them in a styled, scrollable list

---

## 🚀 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/djihane19/anime-recommender.git
cd anime-recommender
```
### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Run the Flask app
```bash
cd app
python app.py
```
### 3. Run the Flask app
```bash
cd app
python app.py
```
