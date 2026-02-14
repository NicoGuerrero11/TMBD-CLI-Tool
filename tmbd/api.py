import os
import requests
from dotenv import load_dotenv
from tmbd.cache import get_cached, set_cache, DEFAULT_TTL, DETAIL_TTL

load_dotenv()

TOKEN = os.getenv("TMDB_API_TOKEN")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}


def safe_request(url: str, ttl: int = DEFAULT_TTL):
    """Hace un request con caché."""
    cached = get_cached(url, ttl)
    if cached is not None:
        return cached

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        set_cache(url, data)
        return data
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Error HTTP al consultar TMDB: {e.response.status_code}") from e
    except requests.exceptions.ConnectionError:
        raise RuntimeError("No se pudo conectar a TMDB")
    except requests.exceptions.Timeout:
        raise RuntimeError("La solicitud a TMDB expiró")
    except requests.exceptions.RequestException as e:
        raise RuntimeError("Error inesperado en la petición") from e


def _encode(query: str) -> str:
    return requests.utils.quote(query)


# --- Películas ---

def get_playing():
    return safe_request(f"{BASE_URL}/movie/now_playing?language=en-US&page=1")


def popular():
    return safe_request(f"{BASE_URL}/movie/popular?language=en-US&page=1")


def top_rated():
    return safe_request(f"{BASE_URL}/movie/top_rated?language=en-US&page=1")


def upcoming():
    return safe_request(f"{BASE_URL}/movie/upcoming?language=en-US&page=1")


def search_movie(query: str):
    return safe_request(f"{BASE_URL}/search/movie?query={_encode(query)}&language=en-US&page=1")


def get_movie_details(movie_id: int):
    return safe_request(f"{BASE_URL}/movie/{movie_id}?language=en-US", ttl=DETAIL_TTL)


# --- Series ---

def search_tv(query: str):
    return safe_request(f"{BASE_URL}/search/tv?query={_encode(query)}&language=en-US&page=1")


def get_tv_details(tv_id: int):
    return safe_request(f"{BASE_URL}/tv/{tv_id}?language=en-US", ttl=DETAIL_TTL)


# --- Personas ---

def search_person(query: str):
    return safe_request(f"{BASE_URL}/search/person?query={_encode(query)}&language=en-US&page=1")


def get_person_details(person_id: int):
    return safe_request(
        f"{BASE_URL}/person/{person_id}?language=en-US&append_to_response=combined_credits",
        ttl=DETAIL_TTL,
    )


# --- Trending ---

def get_trending(media_type: str = "all", time_window: str = "day"):
    return safe_request(f"{BASE_URL}/trending/{media_type}/{time_window}?language=en-US")
