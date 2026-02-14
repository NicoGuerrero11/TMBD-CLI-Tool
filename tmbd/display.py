import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text

console = Console()


def _truncate(text: str, max_len: int = 100) -> str:
    if not text:
        return "N/A"
    return text[:max_len] + "..." if len(text) > max_len else text


def print_json(data):
    """Imprime datos como JSON formateado."""
    console.print_json(json.dumps(data, ensure_ascii=False))


# --- Tablas de listas ---

def display_movies(results: list, title: str, emoji: str):
    """Tabla de películas."""
    table = Table(title=f"{emoji} {title}", show_lines=True)
    table.add_column("#", style="bold cyan", justify="center", width=4)
    table.add_column("\U0001f3ac Título", style="bold white", min_width=20)
    table.add_column("\U0001f4c5 Estreno", style="green", justify="center", width=12)
    table.add_column("\u2b50 Rating", style="yellow", justify="center", width=8)
    table.add_column("\U0001f4dd Sinopsis", style="dim", max_width=50)

    for i, m in enumerate(results, 1):
        table.add_row(
            str(i),
            m.get("title", "N/A"),
            m.get("release_date", "N/A"),
            f"{m.get('vote_average', 0):.1f}",
            _truncate(m.get("overview", "")),
        )
    console.print(table)


def display_tv(results: list, title: str, emoji: str):
    """Tabla de series."""
    table = Table(title=f"{emoji} {title}", show_lines=True)
    table.add_column("#", style="bold cyan", justify="center", width=4)
    table.add_column("\U0001f4fa Nombre", style="bold white", min_width=20)
    table.add_column("\U0001f4c5 Estreno", style="green", justify="center", width=12)
    table.add_column("\u2b50 Rating", style="yellow", justify="center", width=8)
    table.add_column("\U0001f4dd Sinopsis", style="dim", max_width=50)

    for i, s in enumerate(results, 1):
        table.add_row(
            str(i),
            s.get("name", "N/A"),
            s.get("first_air_date", "N/A"),
            f"{s.get('vote_average', 0):.1f}",
            _truncate(s.get("overview", "")),
        )
    console.print(table)


def display_persons(results: list, title: str, emoji: str):
    """Tabla de personas."""
    table = Table(title=f"{emoji} {title}", show_lines=True)
    table.add_column("#", style="bold cyan", justify="center", width=4)
    table.add_column("\U0001f464 Nombre", style="bold white", min_width=20)
    table.add_column("\U0001f3ac Departamento", style="magenta", justify="center", width=14)
    table.add_column("\U0001f525 Popularidad", style="yellow", justify="center", width=12)
    table.add_column("\U0001f31f Conocido por", style="dim", max_width=50)

    for i, p in enumerate(results, 1):
        known_for = ", ".join(
            k.get("title") or k.get("name") or "?"
            for k in p.get("known_for", [])[:3]
        )
        table.add_row(
            str(i),
            p.get("name", "N/A"),
            p.get("known_for_department", "N/A"),
            f"{p.get('popularity', 0):.1f}",
            known_for or "N/A",
        )
    console.print(table)


def display_trending(results: list, title: str, emoji: str):
    """Tabla mixta de trending."""
    table = Table(title=f"{emoji} {title}", show_lines=True)
    table.add_column("#", style="bold cyan", justify="center", width=4)
    table.add_column("\U0001f3f7\ufe0f Tipo", style="magenta", justify="center", width=10)
    table.add_column("\U0001f3ac Nombre", style="bold white", min_width=20)
    table.add_column("\U0001f4c5 Fecha", style="green", justify="center", width=12)
    table.add_column("\u2b50 Rating", style="yellow", justify="center", width=8)

    type_labels = {"movie": "\U0001f3ac Película", "tv": "\U0001f4fa Serie", "person": "\U0001f464 Persona"}

    for i, item in enumerate(results, 1):
        media_type = item.get("media_type", "?")
        name = item.get("title") or item.get("name") or "N/A"
        date = item.get("release_date") or item.get("first_air_date") or "—"
        rating = item.get("vote_average")
        rating_str = f"{rating:.1f}" if rating else "—"

        table.add_row(
            str(i),
            type_labels.get(media_type, media_type),
            name,
            date,
            rating_str,
        )
    console.print(table)


# --- Paneles de detalle ---

def display_movie_detail(data: dict):
    """Panel detallado de una película."""
    genres = ", ".join(g["name"] for g in data.get("genres", []))
    runtime = data.get("runtime", 0)
    hours, mins = divmod(runtime, 60)

    info = Text()
    info.append(f"\U0001f3ac {data.get('title', 'N/A')}", style="bold white")
    if data.get("tagline"):
        info.append(f"\n\U0001f4ac \"{data['tagline']}\"", style="italic dim")
    info.append(f"\n\n\U0001f4c5 Estreno: ", style="bold")
    info.append(f"{data.get('release_date', 'N/A')}", style="green")
    info.append(f"\n\u2b50 Rating: ", style="bold")
    info.append(f"{data.get('vote_average', 0):.1f}/10 ({data.get('vote_count', 0)} votos)", style="yellow")
    info.append(f"\n\u23f1\ufe0f  Duración: ", style="bold")
    info.append(f"{hours}h {mins}m" if runtime else "N/A")
    info.append(f"\n\U0001f3ad Géneros: ", style="bold")
    info.append(genres or "N/A", style="magenta")
    info.append(f"\n\U0001f4b0 Presupuesto: ", style="bold")
    info.append(f"${data.get('budget', 0):,}" if data.get("budget") else "N/A")
    info.append(f"\n\U0001f4b5 Recaudación: ", style="bold")
    info.append(f"${data.get('revenue', 0):,}" if data.get("revenue") else "N/A")
    info.append(f"\n\n\U0001f4dd Sinopsis:\n", style="bold")
    info.append(data.get("overview", "N/A"), style="dim")

    console.print(Panel(info, title=f"\U0001f3ac Detalle de Película", border_style="blue", expand=False))


def display_tv_detail(data: dict):
    """Panel detallado de una serie."""
    genres = ", ".join(g["name"] for g in data.get("genres", []))
    seasons = data.get("number_of_seasons", 0)
    episodes = data.get("number_of_episodes", 0)
    status_map = {
        "Returning Series": "\U0001f7e2 En emisión",
        "Ended": "\U0001f534 Finalizada",
        "Canceled": "\u274c Cancelada",
    }

    info = Text()
    info.append(f"\U0001f4fa {data.get('name', 'N/A')}", style="bold white")
    if data.get("tagline"):
        info.append(f"\n\U0001f4ac \"{data['tagline']}\"", style="italic dim")
    info.append(f"\n\n\U0001f4c5 Estreno: ", style="bold")
    info.append(f"{data.get('first_air_date', 'N/A')}", style="green")
    info.append(f"\n\u2b50 Rating: ", style="bold")
    info.append(f"{data.get('vote_average', 0):.1f}/10 ({data.get('vote_count', 0)} votos)", style="yellow")
    info.append(f"\n\U0001f4fa Temporadas: ", style="bold")
    info.append(f"{seasons} ({episodes} episodios)")
    info.append(f"\n\U0001f4cb Estado: ", style="bold")
    info.append(status_map.get(data.get("status", ""), data.get("status", "N/A")))
    info.append(f"\n\U0001f3ad Géneros: ", style="bold")
    info.append(genres or "N/A", style="magenta")
    info.append(f"\n\n\U0001f4dd Sinopsis:\n", style="bold")
    info.append(data.get("overview", "N/A"), style="dim")

    console.print(Panel(info, title=f"\U0001f4fa Detalle de Serie", border_style="green", expand=False))


def display_person_detail(data: dict):
    """Panel detallado de una persona."""
    credits = data.get("combined_credits", {}).get("cast", [])
    top_credits = sorted(credits, key=lambda x: x.get("popularity", 0), reverse=True)[:5]
    credits_text = "\n".join(
        f"  • {c.get('title') or c.get('name', '?')} ({c.get('release_date', c.get('first_air_date', '?'))[:4]})"
        for c in top_credits
    ) if top_credits else "N/A"

    info = Text()
    info.append(f"\U0001f464 {data.get('name', 'N/A')}", style="bold white")
    info.append(f"\n\n\U0001f3ac Departamento: ", style="bold")
    info.append(data.get("known_for_department", "N/A"), style="magenta")
    info.append(f"\n\U0001f382 Nacimiento: ", style="bold")
    info.append(data.get("birthday", "N/A"), style="green")
    info.append(f"\n\U0001f4cd Lugar: ", style="bold")
    info.append(data.get("place_of_birth", "N/A"))
    info.append(f"\n\U0001f525 Popularidad: ", style="bold")
    info.append(f"{data.get('popularity', 0):.1f}", style="yellow")
    info.append(f"\n\n\U0001f4dd Biografía:\n", style="bold")
    info.append(_truncate(data.get("biography", ""), 300), style="dim")
    info.append(f"\n\n\U0001f31f Trabajos destacados:\n", style="bold")
    info.append(credits_text)

    console.print(Panel(info, title=f"\U0001f464 Detalle de Persona", border_style="magenta", expand=False))
