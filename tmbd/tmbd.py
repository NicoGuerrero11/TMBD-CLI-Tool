import json

import click
from rich.console import Console

from tmbd.api import (
    get_playing,
    popular as fetch_popular,
    top_rated as fetch_top_rated,
    upcoming as fetch_upcoming,
    search_movie,
    search_tv as api_search_tv,
    search_person as api_search_person,
    get_trending as api_get_trending,
    get_movie_details,
    get_tv_details,
    get_person_details,
)
from tmbd.display import (
    display_movies,
    display_tv,
    display_persons,
    display_trending,
    display_movie_detail,
    display_tv_detail,
    display_person_detail,
    print_json,
)
from tmbd.cache import clear_cache

console = Console()


def handle_command(fetch_func, display_func, title, emoji, output_format, *args):
    """Ejecuta un comando y muestra resultados."""
    try:
        data = fetch_func(*args)
        results = data.get("results", [])
        if not results:
            console.print("[yellow]No se encontraron resultados.[/yellow]")
            return
        if output_format == "json":
            print_json(data)
        else:
            display_func(results, title, emoji)
    except RuntimeError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise SystemExit(1)


def handle_detail(fetch_func, display_func, output_format, item_id):
    """Ejecuta un comando de detalle."""
    try:
        data = fetch_func(item_id)
        if output_format == "json":
            print_json(data)
        else:
            display_func(data)
    except RuntimeError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise SystemExit(1)


@click.group()
@click.option("--format", "-f", "output_format", type=click.Choice(["table", "json"]), default="table", help="Formato de salida")
@click.pass_context
def cli(ctx, output_format):
    """\U0001f3ac TMDB CLI - Películas, series y personas desde tu terminal"""
    ctx.ensure_object(dict)
    ctx.obj["format"] = output_format


# --- Películas ---

@cli.command()
@click.pass_context
def playing(ctx):
    """\U0001f3a5 Películas actualmente en cines"""
    handle_command(get_playing, display_movies, "En Cartelera", "\U0001f3a5", ctx.obj["format"])


@cli.command()
@click.pass_context
def popular(ctx):
    """\U0001f525 Películas más populares"""
    handle_command(fetch_popular, display_movies, "Populares", "\U0001f525", ctx.obj["format"])


@cli.command(name="top-rated")
@click.pass_context
def top_rated(ctx):
    """⭐ Películas mejor valoradas"""
    handle_command(fetch_top_rated, display_movies, "Mejor Valoradas", "⭐", ctx.obj["format"])


@cli.command()
@click.pass_context
def upcoming(ctx):
    """\U0001f4c5 Próximos estrenos"""
    handle_command(fetch_upcoming, display_movies, "Próximos Estrenos", "\U0001f4c5", ctx.obj["format"])


# --- Búsquedas ---

@cli.command()
@click.argument("query")
@click.pass_context
def search(ctx, query):
    """\U0001f50d Buscar películas por nombre"""
    handle_command(search_movie, display_movies, f"Películas: '{query}'", "\U0001f50d", ctx.obj["format"], query)


@cli.command(name="search-tv")
@click.argument("query")
@click.pass_context
def search_tv(ctx, query):
    """\U0001f4fa Buscar series por nombre"""
    handle_command(api_search_tv, display_tv, f"Series: '{query}'", "\U0001f4fa", ctx.obj["format"], query)


@cli.command(name="search-person")
@click.argument("query")
@click.pass_context
def search_person(ctx, query):
    """\U0001f464 Buscar actores/personas por nombre"""
    handle_command(api_search_person, display_persons, f"Personas: '{query}'", "\U0001f464", ctx.obj["format"], query)


# --- Trending ---

@cli.command()
@click.option("--type", "-t", "media_type", type=click.Choice(["all", "movie", "tv", "person"]), default="all", help="Tipo de contenido")
@click.option("--window", "-w", "time_window", type=click.Choice(["day", "week"]), default="day", help="Ventana de tiempo")
@click.pass_context
def trending(ctx, media_type, time_window):
    """\U0001f525 Contenido en tendencia"""
    labels = {"day": "Hoy", "week": "Esta Semana"}
    title = f"Trending {labels[time_window]}"

    display_map = {
        "all": display_trending,
        "movie": display_movies,
        "tv": display_tv,
        "person": display_persons,
    }

    handle_command(
        lambda: api_get_trending(media_type, time_window),
        display_map[media_type],
        title,
        "\U0001f525",
        ctx.obj["format"],
    )


# --- Info detallada ---

@cli.group()
@click.pass_context
def info(ctx):
    """\U0001f4cb Información detallada de una película, serie o persona"""
    pass


@info.command(name="movie")
@click.argument("movie_id", type=int)
@click.pass_context
def info_movie(ctx, movie_id):
    """\U0001f3ac Detalle de una película por ID"""
    handle_detail(get_movie_details, display_movie_detail, ctx.obj["format"], movie_id)


@info.command(name="tv")
@click.argument("tv_id", type=int)
@click.pass_context
def info_tv(ctx, tv_id):
    """\U0001f4fa Detalle de una serie por ID"""
    handle_detail(get_tv_details, display_tv_detail, ctx.obj["format"], tv_id)


@info.command(name="person")
@click.argument("person_id", type=int)
@click.pass_context
def info_person(ctx, person_id):
    """\U0001f464 Detalle de una persona por ID"""
    handle_detail(get_person_details, display_person_detail, ctx.obj["format"], person_id)


# --- Caché ---

@cli.command(name="clear-cache")
def cmd_clear_cache():
    """\U0001f9f9 Limpiar caché local"""
    clear_cache()
    console.print("[green]Caché limpiado correctamente.[/green]")


if __name__ == "__main__":
    cli()
