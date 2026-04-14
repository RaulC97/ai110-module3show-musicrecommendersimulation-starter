"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    from src.recommender import load_songs, recommend_songs


WIDTH = 56

# ---------------------------------------------------------------------------
# User profiles
# ---------------------------------------------------------------------------

# Standard profiles
HIGH_ENERGY_POP = {
    "name": "High-Energy Pop",
    "genre": "pop",
    "mood": "happy",
    "energy": 0.90,
    "danceability": 0.85,
}

CHILL_LOFI = {
    "name": "Chill Lofi Study",
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.35,
    "acousticness": 0.75,
}

DEEP_INTENSE_ROCK = {
    "name": "Deep Intense Rock",
    "genre": "rock",
    "mood": "intense",
    "energy": 0.95,
    "tempo_bpm": 150,
}

# Adversarial / edge-case profiles
# 1. Conflicting signals: sad mood but physically high-energy preferences.
#    Sad songs in the CSV are low-energy; numeric fields will pull away from them.
SAD_BUT_HIGH_ENERGY = {
    "name": "Sad but High-Energy [conflicting]",
    "mood": "sad",
    "energy": 0.95,
    "danceability": 0.90,
    "tempo_bpm": 140,
}

# 2. Genre that does not exist in the catalog.
#    Every song scores 0 on genre; winner is decided purely by numeric proximity.
NONEXISTENT_GENRE = {
    "name": "Unknown Genre - 'trap' [no catalog match]",
    "genre": "trap",
    "mood": "confident",
    "energy": 0.80,
}

# 3. Contradictory combo: requests classical music but targets
#    extreme high-energy / fast tempo — the opposite of the one classical
#    song in the catalog (Moonlight Reimagined, energy 0.22, 52 BPM).
CLASSICAL_BUT_FAST = {
    "name": "Classical Fan Wanting Extreme Energy [contradictory]",
    "genre": "classical",
    "energy": 0.97,
    "tempo_bpm": 168,
}

PROFILES = [
    HIGH_ENERGY_POP,
    CHILL_LOFI,
    DEEP_INTENSE_ROCK,
    SAD_BUT_HIGH_ENERGY,
    NONEXISTENT_GENRE,
    CLASSICAL_BUT_FAST,
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_reasons(explanation: str) -> list:
    prefix = "Recommended because: "
    if explanation.startswith(prefix):
        return explanation[len(prefix):].split(", ")
    return [explanation]


def _print_profile_results(profile_name: str, recommendations: list) -> None:
    print("\n" + "=" * WIDTH)
    print(f"  Profile : {profile_name}")
    print(f"  Top {len(recommendations)} Recommendations")
    print("=" * WIDTH)

    for rank, (song, score, explanation) in enumerate(recommendations, 1):
        reasons = _parse_reasons(explanation)
        print(f"\n  #{rank}  {song['title']}")
        print(f"      {song['artist']}  |  {song['genre']}  |  {song['mood']}")
        print(f"      Score : {score:.2f}")
        print(f"      Why   :")
        for reason in reasons:
            print(f"              - {reason}")
        print("  " + "-" * (WIDTH - 2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile in PROFILES:
        # Separate the display name from the scoring keys
        user_prefs = {k: v for k, v in profile.items() if k != "name"}
        recommendations = recommend_songs(user_prefs, songs, k=5)
        _print_profile_results(profile["name"], recommendations)

    print()


if __name__ == "__main__":
    main()
