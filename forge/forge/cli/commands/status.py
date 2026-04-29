from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from forge.core.forge_dir import ForgeDir
from forge.core.logging import setup_logging
from forge.state.store import ForgeStateStore

app = typer.Typer(help="Exibe o status atual do projeto (estado do Forge).")


@app.command()
def show(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
) -> None:
    setup_logging()
    console = Console()

    forge_dir = ForgeDir.from_project_path(path)
    store = ForgeStateStore(forge_dir)
    state = store.load()

    table = Table(title="Forge status")
    table.add_column("Chave", style="bold")
    table.add_column("Valor")

    table.add_row("Projeto", str(forge_dir.project_path))
    table.add_row("Forge dir", str(forge_dir.path))
    table.add_row("Estado", state.phase)
    table.add_row("Etapa", state.step)
    table.add_row("Atualizado em", state.updated_at)

    console.print(table)

