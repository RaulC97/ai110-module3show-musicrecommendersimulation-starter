import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
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
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def _proximity(song_val: float, target: float, threshold: float, max_pts: float) -> float:
    """Score a numeric attribute by how close song_val is to target within threshold."""
    return max(0.0, 1 - abs(song_val - target) / threshold) * max_pts


def _score_song(user: UserProfile, song: Song) -> Tuple[float, List[str]]:
    """
    Score a Song against a UserProfile using the algorithm recipe.

    Scoring breakdown (max 7.5 pts):
      genre match      → +2.0
      mood match       → +1.0
      energy proximity → +1.5  (threshold ±0.20)
      danceability     → +1.0  (threshold ±0.20)
      valence          → +1.0  (threshold ±0.25)
      acousticness     → +0.5  (threshold ±0.25, derived from likes_acoustic bool)
      tempo_bpm        → +0.5  (threshold ±20 BPM)
    """
    score = 0.0
    reasons = []

    # --- Exact match fields ---
    if song.genre == user.favorite_genre:
        score += 2.0
        reasons.append(f"genre matches ({song.genre})")

    if song.mood == user.favorite_mood:
        score += 1.0
        reasons.append(f"mood matches ({song.mood})")

    # --- Numeric proximity fields ---
    energy_pts = _proximity(song.energy, user.target_energy, 0.20, 1.5)
    score += energy_pts
    if energy_pts > 0.5:
        reasons.append(f"energy is close to your target ({user.target_energy:.2f})")

    # UserProfile expresses acousticness as a bool; map to a target value
    target_acousticness = 0.8 if user.likes_acoustic else 0.2
    acousticness_pts = _proximity(song.acousticness, target_acousticness, 0.25, 0.5)
    score += acousticness_pts
    if acousticness_pts > 0.15:
        pref = "acoustic" if user.likes_acoustic else "non-acoustic"
        reasons.append(f"sound texture fits your {pref} preference")

    return score, reasons


def _score_song_dict(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Score a song dict against a user_prefs dict using the full algorithm recipe.
    Supports optional keys: genre, mood, energy, danceability, valence, acousticness, tempo_bpm.
    """
    score = 0.0
    reasons = []

    if user_prefs.get("genre") and song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append(f"genre matches ({song['genre']})")

    if user_prefs.get("mood") and song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append(f"mood matches ({song['mood']})")

    if "energy" in user_prefs:
        pts = _proximity(song["energy"], user_prefs["energy"], 0.20, 1.5)
        score += pts
        if pts > 0.5:
            reasons.append(f"energy is a close match")

    if "danceability" in user_prefs:
        pts = _proximity(song["danceability"], user_prefs["danceability"], 0.20, 1.0)
        score += pts
        if pts > 0.4:
            reasons.append("danceability fits your preference")

    if "valence" in user_prefs:
        pts = _proximity(song["valence"], user_prefs["valence"], 0.25, 1.0)
        score += pts
        if pts > 0.4:
            reasons.append("emotional tone matches")

    if "acousticness" in user_prefs:
        pts = _proximity(song["acousticness"], user_prefs["acousticness"], 0.25, 0.5)
        score += pts
        if pts > 0.15:
            reasons.append("acoustic texture fits")

    if "tempo_bpm" in user_prefs:
        pts = _proximity(song["tempo_bpm"], user_prefs["tempo_bpm"], 20, 0.5)
        score += pts
        if pts > 0.2:
            reasons.append("tempo is close to your preference")

    return score, reasons


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = [(_score_song(user, song)[0], song) for song in self.songs]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [song for _, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = _score_song(user, song)
        if reasons:
            return "Recommended because: " + ", ".join(reasons)
        return "Matched based on overall profile similarity"


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = _score_song_dict(user_prefs, song)
        explanation = "Recommended because: " + ", ".join(reasons) if reasons else "Matched on overall profile"
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
