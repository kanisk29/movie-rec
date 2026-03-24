# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on their attributes such as genres, keywords, cast, and crew.

---

## Overview

This project builds a recommendation engine by processing movie-related metadata and transforming it into a structured format suitable for similarity comparison.

The workflow includes:
- Data preprocessing
- Feature extraction
- Data transformation
- Preparation for similarity computation

---

## Features

- Cleans and preprocesses raw movie data
- Handles missing values and removes duplicates
- Extracts relevant information from structured fields
- Converts complex string data into usable formats
- Selects top cast members for better recommendations
- Prepares combined feature sets for similarity analysis

---

## Data Processing Steps

1. Merge datasets based on movie title
2. Remove unnecessary columns
3. Handle missing values by dropping incomplete rows
4. Convert JSON-like strings into Python lists using parsing
5. Extract:
   - Genre names
   - Keywords
   - Top 3 cast members
   - Relevant crew members
6. Ensure clean and consistent structure for further processing

---

## Technologies Used

- Python
- Pandas
- NumPy
- AST (for parsing structured strings)

---


---

## How It Works

- Each movie is represented as a combination of its features
- These features are later used to compute similarity between movies
- Based on similarity scores, the system can recommend movies that are most alike

---

## Future Improvements

- Add vectorization (e.g., Bag of Words / TF-IDF)
- Implement cosine similarity for recommendations
- Build a user interface for interaction
- Deploy as a web application
