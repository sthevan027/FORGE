from __future__ import annotations

import typer
from rich.console import Console

from forge.ai import factory as ai_factory
from forge.bots.dev import DevBot
from forge.core.forge_dir import ForgeDir
from forge.core.logging import get_logger, setup_logging
from forge.state.machine import ForgeFlowError, ForgeStateMachine

dev_app = typer.Typer(help="Comandos do Dev Bot (MVP).")


@dev_app.command("run")
def dev_run(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
) -> None:
    setup_logging()
    log = get_logger()
    console = Console()
    forge_dir = ForgeDir.from_project_path(path)

    plan_path = forge_dir.plan_file()
    if not plan_path.exists():
        console.print("[red]Plano não encontrado. Rode:[/red] forge plan")
        raise typer.Exit(code=1)

    plan_text = plan_path.read_text(encoding="utf-8")
    try:
        adapter = ai_factory.get_adapter(forge_dir)
        dev_bot = DevBot(adapter)
        output = dev_bot.run(forge_dir, plan_text)
        dev_bot.write_output(forge_dir, output)
        machine = ForgeStateMachine(forge_dir)
        machine.after_dev_run()
    except ForgeFlowError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1)
    except Exception as exc:  # noqa: BLE001
        console.print(f"[red]Erro no Dev Bot:[/red] {exc}")
        log.error("Erro no Dev Bot", error=str(exc))
        raise typer.Exit(code=1)

    console.print("[green]Saída do Dev gravada em[/green]", str(forge_dir.dev_output_file()))
    log.info("Dev run concluído", output=str(forge_dir.dev_output_file()))
