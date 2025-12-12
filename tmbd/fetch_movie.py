import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TMDB_API_TOKEN")

def safe_request(url: str, header:dict):
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise RuntimeError("Error HTTP al consultar TMDB") from e

    except requests.exceptions.ConnectionError:
        raise RuntimeError("No se pudo conectar a TMDB")

    except requests.exceptions.Timeout:
        raise RuntimeError("La solicitud a TMDB expiró")

    except requests.exceptions.RequestException as e:
        raise RuntimeError("Error inesperado en la petición") from e

def get_playing():
    url_playing = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN} ",
    }

    return safe_request(url_playing, headers)

def popular():
    url_popular = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    return safe_request(url_popular, headers)
def top_rated():
    url_top = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    return safe_request(url_top, headers)

def upcoming():
    url_upcoming = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    return safe_request(url_upcoming, headers)
