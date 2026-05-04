from __future__ import annotations

import typer
from rich.console import Console

from forge.ai import factory as ai_factory
from forge.bots.engineer import EngineerBot
from forge.core.forge_dir import ForgeDir
from forge.core.logging import get_logger, setup_logging
from forge.state.machine import ForgeFlowError, ForgeStateMachine


def run(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
) -> None:
    setup_logging()
    log = get_logger()
    console = Console()
    forge_dir = ForgeDir.from_project_path(path)

    if not forge_dir.state_file().exists():
        console.print("[red]Projeto não inicializado. Rode: forge init --path ...[/red]")
        raise typer.Exit(code=1)

    briefing_path = forge_dir.briefing_file()
    if not briefing_path.exists():
        console.print("[red]Arquivo de briefing não encontrado:[/red]", str(briefing_path))
        raise typer.Exit(code=1)

    briefing_text = briefing_path.read_text(encoding="utf-8")
    try:
        adapter = ai_factory.get_adapter(forge_dir)
        engineer = EngineerBot(adapter)
        plan_md = engineer.generate_plan(forge_dir, briefing_text)
        engineer.write_plan(forge_dir, plan_md)
        machine = ForgeStateMachine(forge_dir)
        machine.after_plan()
    except ForgeFlowError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1)
    except Exception as exc:  # noqa: BLE001
        console.print(f"[red]Erro ao gerar plano:[/red] {exc}")
        log.error("Erro ao gerar plano", error=str(exc))
        raise typer.Exit(code=1)

    console.print("[green]Plano gerado em[/green]", str(forge_dir.plan_file()))
    log.info("Plano gerado", plan=str(forge_dir.plan_file()))
