from __future__ import annotations

import typer
from rich.console import Console
from rich.prompt import Confirm

from forge.core.forge_dir import ForgeDir
from forge.core.logging import get_logger, setup_logging
from forge.state.machine import ForgeFlowError, ForgeStateMachine

approve_app = typer.Typer(help="Aprovar artefatos do workflow.")


@approve_app.command("plan")
def approve_plan(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
    yes: bool = typer.Option(False, "--yes", "-y", help="Aprova sem confirmar interativamente."),
) -> None:
    setup_logging()
    log = get_logger()
    console = Console()
    forge_dir = ForgeDir.from_project_path(path)

    if not yes and not Confirm.ask("Aprovar o plano atual e seguir para implementação?"):
        console.print("[yellow]Aprovação cancelada.[/yellow]")
        raise typer.Exit(code=0)

    try:
        machine = ForgeStateMachine(forge_dir)
        machine.after_approve_plan()
    except ForgeFlowError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1)

    console.print("[green]Plano aprovado. Próximo passo:[/green] forge dev run")
    log.info("Plano aprovado")
