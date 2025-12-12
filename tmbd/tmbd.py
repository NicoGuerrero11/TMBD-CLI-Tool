import argparse
import json
from fetch_movie import get_playing, popular, top_rated, upcoming

def main():
    parser = argparse.ArgumentParser(description='TMDB CLI')
    parser.add_argument(
        '--type',
        required=True,
        choices=["playing", "popular", "top_rated", "upcoming"],
        help='The type of movie to get'
    )

    args = parser.parse_args()

    try:
        if args.type == "playing":
            data = get_playing()
        elif args.type == "popular":
            data = popular()
        elif args.type == "top_rated":
            data = top_rated()
        elif args.type == "upcoming":
            data = upcoming()
        print(json.dumps(data, indent=2))
    except RuntimeError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()