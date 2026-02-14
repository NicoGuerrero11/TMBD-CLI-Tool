# 🎨 TMDB-CLI

Una herramienta de línea de comandos simple y elegante para consultar información de películas desde **The Movie Database (TMDB)**, con tablas coloridas en tu terminal.

## ✨ Características

- 🎥 **Now Playing**: Películas que están actualmente en cines
- 🔥 **Popular**: Las películas más populares del momento
- ⭐ **Top Rated**: Las películas mejor valoradas de todos los tiempos
- 🔜 **Upcoming**: Próximos estrenos
- 🔍 **Search**: Buscar películas por nombre
- 🎨 **Rich Tables**: Resultados en tablas coloridas con emojis

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

2. **Instala como paquete** (recomendado):
   ```bash
   pip install -e .
   ```

   O instala solo las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu API Token**:

   Crea un archivo `.env` en la raíz del proyecto y agrega tu token:
   ```env
   TMDB_API_TOKEN=tu_token_aqui
   ```

   Para obtener tu token:
   - Ve a [TMDB](https://www.themoviedb.org/)
   - Regístrate o inicia sesión
   - Ve a Configuración → API → Crear Bearer Token

## 💻 Uso

Si instalaste con `pip install -e .`:

```bash
tmbd <comando>
```

O directamente con Python:

```bash
python -m tmbd.tmbd <comando>
```

### Comandos disponibles:

- `playing` — Películas actualmente en cines
- `popular` — Películas populares
- `top-rated` — Películas mejor valoradas
- `upcoming` — Próximos estrenos
- `search <query>` — Buscar películas por nombre

### Ejemplos:

```bash
# Películas en cartelera
tmbd playing

# Películas populares
tmbd popular

# Películas mejor valoradas
tmbd top-rated

# Próximos estrenos
tmbd upcoming

# Buscar películas
tmbd search "Inception"
```

### Ejemplo de salida:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                    🔍 Resultados: 'Inception'                    ┃
┡━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ #  │ 🎨 Título           │ 📅 Estreno │ ⭐ Rat │ 📝 Sinopsis                  │
│ 1  │ Inception           │ 2010-07-15 │  8.4   │ A thief who steals...     │
└────┴─────────────────────┴────────────┴────────┴────────────────────────────┘
```

## 📦 Estructura del Proyecto

```
TMBD-CLI-Tool/
├── .env                    # Variables de entorno (API Token)
├── README.md               # Este archivo
├── requirements.txt        # Dependencias del proyecto
├── setup.py                # Configuración de instalación
└── tmbd/
    ├── __init__.py         # Paquete Python
    ├── tmbd.py             # CLI con Click + Rich
    └── fetch_movie.py      # Funciones para consultar la API de TMDB
```

## 🔧 Cómo Funciona

1. **tmbd.py**: CLI construido con [Click](https://click.palletsprojects.com/) con subcomandos intuitivos
2. **fetch_movie.py**: Peticiones HTTP a la API de TMDB usando `requests`
3. **Rich**: Resultados mostrados en tablas coloridas con [Rich](https://rich.readthedocs.io/)
4. **Manejo de errores**: Errores HTTP, conexión, timeout y otros errores manejados de forma amigable

## 🛡️ Manejo de Errores

El CLI incluye manejo de errores para:
- ❌ Errores HTTP (401, 404, 500, etc.)
- 🔌 Problemas de conexión
- ⏱️ Timeouts
- 🐛 Errores inesperados

Todos los errores se muestran de forma amigable en la terminal.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras un bug o tienes una sugerencia:

1. Abre un issue
2. Crea un fork del proyecto
3. Haz tus cambios
4. Envía un pull request

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🔗 Recursos

- [Documentación de TMDB API](https://developers.themoviedb.org/3)
- [The Movie Database](https://www.themoviedb.org/)

---

**https://roadmap.sh/projects/tmdb-cli**
