# 🎨 TMDB-CLI

Herramienta de línea de comandos para buscar **películas, series y actores** usando la API de The Movie Database, con interfaz colorida y profesional.

> 💡 **Destaca**: UX con tablas coloridas, caché local y múltiples formatos de salida

## ✨ Características

- 🎥 **Películas**: En cartelera, populares, mejor valoradas, próximos estrenos
- 📺 **Series**: Búsqueda e información detallada de series de TV
- 👤 **Personas**: Búsqueda de actores, directores y más
- 🔥 **Trending**: Contenido en tendencia (día/semana)
- 📋 **Info detallada**: Paneles con ratings, géneros, biografías y créditos
- 🎨 **Rich Tables**: Interfaz colorida con [Rich](https://rich.readthedocs.io/)
- 📦 **Caché local**: Respuestas cacheadas para mayor velocidad
- 📄 **Múltiples formatos**: Salida en tabla o JSON (`--format json`)

## 📋 Requisitos Previos

- Python 3.7 o superior
- Una cuenta en [TMDB](https://www.themoviedb.org/)
- API Token de TMDB (Bearer Token)

## 🚀 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <tu-repositorio>
   cd TMBD-CLI-Tool
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu API Token**:

   Crea un archivo `.env` en la raíz del proyecto:
   ```env
   TMDB_API_TOKEN=tu_token_aqui
   ```

## 💻 Uso

```bash
python -m tmbd [--format table|json] <comando>
```

### Comandos disponibles:

**Películas:**
- `python -m tmbd playing` — En cartelera
- `python -m tmbd popular` — Populares
- `python -m tmbd top-rated` — Mejor valoradas
- `python -m tmbd upcoming` — Próximos estrenos

**Búsqueda:**
- `python -m tmbd search <query>` — Buscar películas
- `python -m tmbd search-tv <query>` — Buscar series
- `python -m tmbd search-person <query>` — Buscar actores/personas

**Trending:**
- `python -m tmbd trending` — Tendencia del día (todo)
- `python -m tmbd trending --type movie --window week` — Películas de la semana

**Info detallada:**
- `python -m tmbd info movie <id>` — Detalle de película
- `python -m tmbd info tv <id>` — Detalle de serie
- `python -m tmbd info person <id>` — Detalle de persona

**Utilidades:**
- `python -m tmbd clear-cache` — Limpiar caché local

> 💡 **Tip**: Si prefieres usar `tmbd` directamente, instala con `pip install -e .` y asegúrate de que el directorio de scripts de pip esté en tu PATH.

### Ejemplos:

```bash
# Películas en cartelera
python -m tmbd playing

# Buscar series
python -m tmbd search-tv "Breaking Bad"

# Buscar actores
python -m tmbd search-person "Leonardo DiCaprio"

# Trending de la semana (solo películas)
python -m tmbd trending --type movie --window week

# Info detallada de una película
python -m tmbd info movie 27205

# Info de un actor
python -m tmbd info person 6193

# Salida en JSON
python -m tmbd --format json search "Inception"
```

## 📦 Estructura del Proyecto

```
TMBD-CLI-Tool/
├── .env                    # Variables de entorno (API Token)
├── README.md               # Este archivo
├── requirements.txt        # Dependencias
├── setup.py                # Configuración de instalación
└── tmbd/
    ├── __init__.py         # Paquete Python
    ├── __main__.py         # Entry point para python -m tmbd
    ├── tmbd.py             # CLI con Click (comandos)
    ├── api.py              # Requests a TMDB con caché
    ├── display.py          # Tablas y paneles Rich
    └── cache.py            # Sistema de caché local
```

## 🔧 Cómo Funciona

1. **tmbd.py**: CLI con [Click](https://click.palletsprojects.com/) — comandos para películas, series, personas y trending
2. **api.py**: Peticiones a TMDB con caché automático (30 min listas, 24h detalles)
3. **display.py**: Tablas y paneles coloridos con [Rich](https://rich.readthedocs.io/)
4. **cache.py**: Caché local en `~/.tmbd_cache/` con TTL configurable

## 🛡️ Manejo de Errores

- ❌ Errores HTTP (401, 404, 500, etc.)
- 🔌 Problemas de conexión
- ⏱️ Timeouts
- 🐛 Errores inesperados

## 🔗 Recursos

- [Documentación de TMDB API](https://developers.themoviedb.org/3)
- [The Movie Database](https://www.themoviedb.org/)

---

**https://roadmap.sh/projects/tmdb-cli**
