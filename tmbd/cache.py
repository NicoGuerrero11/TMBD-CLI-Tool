import hashlib
import json
import os
import time
from pathlib import Path

CACHE_DIR = Path.home() / ".tmbd_cache"
DEFAULT_TTL = 1800  # 30 minutos para listas
DETAIL_TTL = 86400  # 24 horas para detalles


def _ensure_cache_dir():
    CACHE_DIR.mkdir(exist_ok=True)


def _cache_key(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()


def get_cached(url: str, ttl: int = DEFAULT_TTL):
    """Retorna datos cacheados si existen y no han expirado."""
    _ensure_cache_dir()
    cache_file = CACHE_DIR / f"{_cache_key(url)}.json"

    if not cache_file.exists():
        return None

    try:
        data = json.loads(cache_file.read_text())
        if time.time() - data["timestamp"] < ttl:
            return data["response"]
    except (json.JSONDecodeError, KeyError):
        cache_file.unlink(missing_ok=True)

    return None


def set_cache(url: str, response: dict):
    """Guarda una respuesta en caché."""
    _ensure_cache_dir()
    cache_file = CACHE_DIR / f"{_cache_key(url)}.json"
    cache_file.write_text(json.dumps({
        "timestamp": time.time(),
        "url": url,
        "response": response,
    }))


def clear_cache():
    """Limpia todo el caché."""
    if CACHE_DIR.exists():
        for f in CACHE_DIR.glob("*.json"):
            f.unlink()
