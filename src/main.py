"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:

    songs = load_songs("data/songs.csv")

    # User profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_valence": 0.8,
        "target_danceability": 0.8,
        "target_acousticness": 0.2,
        "target_tempo_bpm": 120,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n🎵 Top Recommendations:\n")

    for song, score, explanation in recommendations:

        print(f"Title: {song['title']}")
        print(f"Artist: {song['artist']}")
        print(f"Genre: {song['genre']}")
        print(f"Score: {score:.2f}")
        print(f"Reasons: {explanation}")
        print("-" * 50)


if __name__ == "__main__":
    main()