import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py.
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py.
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs for a user."""
        scored_songs = []

        for song in self.songs:
            song_dict = song.__dict__
            user_dict = {
                "favorite_genre": user.favorite_genre,
                "favorite_mood": user.favorite_mood,
                "target_energy": user.target_energy,
                "target_valence": 0.60,
                "target_danceability": 0.60,
                "target_acousticness": 0.80 if user.likes_acoustic else 0.20,
                "target_tempo_bpm": 80,
            }

            score, reasons = score_song(user_dict, song_dict)
            scored_songs.append((song, score, reasons))

        scored_songs.sort(key=lambda item: item[1], reverse=True)
        return [song for song, score, reasons in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended."""
        song_dict = song.__dict__
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_valence": 0.60,
            "target_danceability": 0.60,
            "target_acousticness": 0.80 if user.likes_acoustic else 0.20,
            "target_tempo_bpm": 80,
        }

        score, reasons = score_song(user_dict, song_dict)
        return f"Score: {score:.2f}. Reasons: {', '.join(reasons)}"


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric values."""
    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }

            songs.append(song)

    return songs


def similarity_score(user_target: float, song_value: float, max_points: float) -> float:
    """Score numeric similarity where closer values earn more points."""
    difference = abs(user_target - song_value)
    score = max_points * (1 - difference)
    return max(score, 0)


def tempo_similarity_score(user_target: float, song_value: float, max_points: float) -> float:
    """Score tempo similarity using a normalized BPM difference."""
    difference = abs(user_target - song_value)
    normalized_difference = min(difference / 100, 1)
    score = max_points * (1 - normalized_difference)
    return max(score, 0)


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return reasons."""
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_points = similarity_score(
        user_prefs["target_energy"],
        song["energy"],
        1.5
    )
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    valence_points = similarity_score(
        user_prefs.get("target_valence", 0.60),
        song["valence"],
        1.0
    )
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    danceability_points = similarity_score(
        user_prefs.get("target_danceability", 0.60),
        song["danceability"],
        0.75
    )
    score += danceability_points
    reasons.append(f"danceability similarity (+{danceability_points:.2f})")

    acousticness_points = similarity_score(
        user_prefs.get("target_acousticness", 0.80),
        song["acousticness"],
        0.75
    )
    score += acousticness_points
    reasons.append(f"acousticness similarity (+{acousticness_points:.2f})")

    tempo_points = tempo_similarity_score(
        user_prefs.get("target_tempo_bpm", 80),
        song["tempo_bpm"],
        0.5
    )
    score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Score all songs, rank them, and return the top k recommendations."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_songs[:k]