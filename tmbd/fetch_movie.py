import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TMDB_API_TOKEN")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}


def safe_request(url: str):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Error HTTP al consultar TMDB: {e.response.status_code}") from e
    except requests.exceptions.ConnectionError:
        raise RuntimeError("No se pudo conectar a TMDB")
    except requests.exceptions.Timeout:
        raise RuntimeError("La solicitud a TMDB expiró")
    except requests.exceptions.RequestException as e:
        raise RuntimeError("Error inesperado en la petición") from e


def get_playing():
    return safe_request(f"{BASE_URL}/movie/now_playing?language=en-US&page=1")


def popular():
    return safe_request(f"{BASE_URL}/movie/popular?language=en-US&page=1")


def top_rated():
    return safe_request(f"{BASE_URL}/movie/top_rated?language=en-US&page=1")


def upcoming():
    return safe_request(f"{BASE_URL}/movie/upcoming?language=en-US&page=1")


def search_movie(query: str):
    encoded_query = requests.utils.quote(query)
    return safe_request(f"{BASE_URL}/search/movie?query={encoded_query}&language=en-US&page=1")
