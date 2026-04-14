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


WIDTH = 54

def _parse_reasons(explanation: str) -> list:
    prefix = "Recommended because: "
    if explanation.startswith(prefix):
        return explanation[len(prefix):].split(", ")
    return [explanation]


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * WIDTH)
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


if __name__ == "__main__":
    main()
