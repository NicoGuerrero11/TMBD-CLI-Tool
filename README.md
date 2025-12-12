# 🎬 TMDB-CLI

Una herramienta de línea de comandos simple y elegante para consultar información de películas desde **The Movie Database (TMDB)**.

## ✨ Características

Este CLI te permite acceder rápidamente a diferentes listas de películas directamente desde tu terminal:

- 🎥 **Now Playing**: Películas que están actualmente en cines
- 🔥 **Popular**: Las películas más populares del momento
- ⭐ **Top Rated**: Las películas mejor valoradas de todos los tiempos
- 🔜 **Upcoming**: Próximos estrenos

## 📋 Requisitos Previos

- Python 3.7 o superior
- Una cuenta en [TMDB](https://www.themoviedb.org/)
- API Token de TMDB (Bearer Token)

## 🚀 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <tu-repositorio>
   cd TMBD-CLI
   ```

2. **Instala las dependencias**:
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

Ejecuta el CLI con el siguiente formato:

```bash
python tmbd/tmbd.py --type <tipo_de_consulta>
```

### Opciones disponibles:

| Opción | Descripción |
|--------|-------------|
| `playing` | Películas actualmente en cines |
| `popular` | Películas populares |
| `top_rated` | Películas mejor valoradas |
| `upcoming` | Próximos estrenos |

### Ejemplos:

```bash
# Obtener películas en cartelera
python tmbd/tmbd.py --type playing

# Obtener películas populares
python tmbd/tmbd.py --type popular

# Obtener películas mejor valoradas
python tmbd/tmbd.py --type top_rated

# Obtener próximos estrenos
python tmbd/tmbd.py --type upcoming
```

## 📦 Estructura del Proyecto

```
TMBD-CLI/
├── .env                    # Variables de entorno (API Token)
├── README.md              # Este archivo
├── requirements.txt       # Dependencias del proyecto
└── tmbd/
    ├── tmbd.py           # Punto de entrada del CLI
    └── fetch_movie.py    # Funciones para consultar la API de TMDB
```

## 🔧 Cómo Funciona

1. **tmbd.py**: Maneja los argumentos de línea de comandos usando `argparse` y llama a las funciones correspondientes
2. **fetch_movie.py**: Contiene las funciones que hacen las peticiones HTTP a la API de TMDB usando `requests`
3. **Manejo de errores**: Incluye manejo robusto de errores HTTP, conexión, timeout y otros errores inesperados
4. **Salida**: Los resultados se imprimen en formato JSON con indentación legible

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

**Hecho con ❤️ para los amantes del cine**
