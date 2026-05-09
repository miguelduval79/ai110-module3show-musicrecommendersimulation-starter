# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Goal / Task

This recommender system suggests songs based on a user's musical preferences. It compares song attributes such as genre, mood, energy, valence, danceability, acousticness, and tempo to a user's preferred listening style.

The goal is to simulate how recommendation systems like Spotify or YouTube Music generate personalized recommendations.

---

## 3. Data Used

The dataset contains 19 songs stored in `data/songs.csv`.

Each song includes:
- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

The dataset includes multiple genres and moods such as:
- pop
- lofi
- rock
- synthwave
- classical
- latin
- edm
- jazz

One limitation is that the dataset is still very small compared to real-world recommendation systems.

---

## 4. Algorithm Summary

The recommender uses a content-based filtering approach.

Each song receives points based on:
- genre match
- mood match
- similarity between song energy and user target energy
- similarity between valence, danceability, acousticness, and tempo

Genre and mood matches receive the largest score boosts because they strongly shape the listening experience.

Songs are ranked from highest score to lowest score, and the top songs become recommendations.

---

## 5. Observed Behavior / Biases

The recommender tends to prioritize genre and mood heavily. This can sometimes overpower other numerical features.

For example, the "Conflicting Sad Energy" profile requested high energy and sad/classical music. The recommender still ranked "Rainy Window" first because it matched the classical genre and sad mood even though its energy was low.

The system can also create small filter bubbles where songs from one genre dominate the recommendations repeatedly.

Because the dataset is limited, some genres have fewer songs available, which affects recommendation diversity.

---

## 6. Evaluation Process

The recommender was tested using several user profiles:
- High-Energy Happy Pop
- Chill Focus Lofi
- Deep Intense Rock
- Conflicting Sad Energy

The system generally behaved logically:
- pop profiles returned upbeat pop songs
- lofi profiles returned calm study music
- rock profiles returned intense high-energy songs

One experiment showed that changing scoring weights significantly changes the ranking behavior. This demonstrated how sensitive recommendation systems are to algorithm design choices.

---

## 7. Intended Use and Non-Intended Use

### Intended Use

This project is designed for:
- educational exploration
- learning recommendation system concepts
- understanding scoring and ranking logic
- demonstrating simple AI-style personalization

### Non-Intended Use

This system should not be used:
- for real music streaming services
- for large-scale production recommendations
- to model complex human emotions or musical taste
- as a replacement for human-curated recommendations

The dataset and algorithm are too small and simplified for real-world deployment.

---

## 8. Ideas for Improvement

Possible improvements include:
- adding a much larger dataset
- introducing collaborative filtering between users
- adding lyric analysis
- balancing recommendation diversity
- improving tempo and emotional similarity calculations
- adding machine learning ranking models

---

## 9. Personal Reflection

The biggest learning moment in this project was realizing that recommendation systems are mostly similarity engines. The AI does not actually understand music emotionally. Instead, it compares numbers and categories to estimate what a user may enjoy.

Using AI tools helped speed up coding, debugging, and brainstorming ideas. However, I still needed to verify the logic manually because AI suggestions sometimes introduced incorrect assumptions or unrealistic implementations.

One surprising part of the project was how simple scoring systems can still feel intelligent. Even basic rules created recommendations that looked realistic and personalized.

If I continued this project, I would experiment with collaborative filtering, larger datasets, and possibly a Streamlit frontend so users could interact with the recommender visually.