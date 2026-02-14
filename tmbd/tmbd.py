import click
from rich.console import Console
from rich.table import Table
from tmbd.fetch_movie import (
    get_playing,
    popular as fetch_popular,
    top_rated as fetch_top_rated,
    upcoming as fetch_upcoming,
    search_movie,
)

console = Console()


def display_movies(movies: list, title: str, emoji: str):
    """Muestra películas en una tabla Rich."""
    table = Table(title=f"{emoji} {title}", show_lines=True)
    table.add_column("#", style="bold cyan", justify="center", width=4)
    table.add_column("🎬 Título", style="bold white", min_width=20)
    table.add_column("📅 Estreno", style="green", justify="center", width=12)
    table.add_column("⭐ Rating", style="yellow", justify="center", width=8)
    table.add_column("📝 Sinopsis", style="dim", max_width=50)

    for i, movie in enumerate(movies, 1):
        synopsis = movie.get("overview", "N/A")
        if len(synopsis) > 100:
            synopsis = synopsis[:100] + "..."
        table.add_row(
            str(i),
            movie.get("title", "N/A"),
            movie.get("release_date", "N/A"),
            f"{movie.get('vote_average', 0):.1f}",
            synopsis,
        )

    console.print(table)


def handle_command(fetch_func, title, emoji, *args):
    """Ejecuta un comando y muestra resultados."""
    try:
        data = fetch_func(*args)
        movies = data.get("results", [])
        if not movies:
            console.print(f"[yellow]No se encontraron películas.[/yellow]")
            return
        display_movies(movies, title, emoji)
    except RuntimeError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise SystemExit(1)


@click.group()
def cli():
    """\U0001f3ac TMDB CLI - Consulta películas desde tu terminal"""
    pass


@cli.command()
def playing():
    """\U0001f3a5 Películas actualmente en cines"""
    handle_command(get_playing, "En Cartelera", "\U0001f3a5")


@cli.command()
def popular():
    """\U0001f525 Películas más populares"""
    handle_command(fetch_popular, "Populares", "\U0001f525")


@cli.command(name="top-rated")
def top_rated():
    """⭐ Películas mejor valoradas"""
    handle_command(fetch_top_rated, "Mejor Valoradas", "⭐")


@cli.command()
def upcoming():
    """\U0001f4c5 Próximos estrenos"""
    handle_command(fetch_upcoming, "Próximos Estrenos", "\U0001f4c5")


@cli.command()
@click.argument("query")
def search(query):
    """\U0001f50d Buscar películas por nombre"""
    handle_command(search_movie, f"Resultados: '{query}'", "\U0001f50d", query)


if __name__ == "__main__":
    cli()
