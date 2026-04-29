from __future__ import annotations

import typer
from rich.console import Console

from forge.core.forge_dir import ForgeDir
from forge.core.logging import read_log_file, setup_logging

app = typer.Typer(help="Exibe logs do Forge para o projeto atual.")


@app.command()
def show(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
    tail: int = typer.Option(200, "--tail", help="Número máximo de linhas para mostrar."),
) -> None:
    setup_logging()
    console = Console()

    forge_dir = ForgeDir.from_project_path(path)
    lines = read_log_file(forge_dir, tail=tail)
    if not lines:
        console.print("[yellow]Sem logs ainda.[/yellow]")
        raise typer.Exit(code=0)

    console.print("".join(lines))

