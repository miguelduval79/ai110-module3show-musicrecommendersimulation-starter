# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a simplified music recommendation system inspired by platforms like Spotify and YouTube. The recommender uses a content-based filtering approach to compare song attributes with a user's musical preferences in order to generate personalized recommendations.

The system analyzes features such as genre, mood, energy, tempo, valence, danceability, and acousticness. Each song receives a score based on how closely it matches the user's preferred musical vibe. Songs are then ranked from highest score to lowest score to generate recommendations.

The goal of this project is to understand how recommendation systems transform user preferences and song data into predictions, while also exploring the limitations, bias, and tradeoffs involved in AI-driven personalization systems.

## How The System Works

This recommender system uses a content-based filtering approach to recommend songs based on a user's musical preferences. Instead of comparing users to other listeners, the system compares song attributes directly to a user's preferred features.

Each song contains data such as genre, mood, energy, tempo, valence, danceability, and acousticness. The recommender compares these attributes against a user profile and assigns a score to each song based on similarity.

The system prioritizes genre and mood matches because they define the overall musical vibe more strongly than numerical attributes alone. Numerical features like energy and valence are also used to reward songs that are closer to the user's preferred intensity and emotional tone.

After each song receives a score, the recommender ranks the songs from highest score to lowest score and returns the best matches.

### Features Used

- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

### User Profile Data

The user profile stores preferences such as:

- favorite genre
- preferred mood
- preferred energy level
- preferred tempo range

### Recommendation Logic

The recommender calculates a score for every song.

Examples:
- matching genre = high score boost
- matching mood = medium to high score boost
- similar energy and valence = additional points

Songs with the highest scores become recommendations.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

