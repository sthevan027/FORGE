from __future__ import annotations

import typer
from rich.console import Console

from forge.ai import factory as ai_factory
from forge.bots.engineer import EngineerBot
from forge.core.forge_dir import ForgeDir
from forge.core.logging import get_logger, setup_logging
from forge.state.machine import ForgeFlowError, ForgeStateMachine

engineer_app = typer.Typer(help="Comandos do Engenheiro IA.")


@engineer_app.command("review")
def engineer_review(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
) -> None:
    setup_logging()
    log = get_logger()
    console = Console()
    forge_dir = ForgeDir.from_project_path(path)

    qa_path = forge_dir.qa_report_file()
    if not qa_path.exists():
        console.print("[red]Relatório de QA não encontrado. Rode:[/red] forge qa run")
        raise typer.Exit(code=1)

    qa_report = qa_path.read_text(encoding="utf-8")
    extra = ""
    dev_path = forge_dir.dev_output_file()
    if dev_path.exists():
        extra = "Trecho da entrega do Dev:\n\n" + dev_path.read_text(encoding="utf-8")[:8000]

    try:
        adapter = ai_factory.get_adapter(forge_dir)
        engineer = EngineerBot(adapter)
        result = engineer.review(forge_dir, qa_report, extra_context=extra)
        engineer.write_decision(forge_dir, result.raw)
        machine = ForgeStateMachine(forge_dir)
        machine.after_engineer_review(approved=result.approved)
    except ForgeFlowError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1)
    except Exception as exc:  # noqa: BLE001
        console.print(f"[red]Erro na revisão do Engenheiro:[/red] {exc}")
        log.error("Erro na revisão do Engenheiro", error=str(exc))
        raise typer.Exit(code=1)

    decision_path = forge_dir.engineer_decision_file()
    if result.approved:
        console.print("[green]Revisão: aprovada. Decisão em[/green]", str(decision_path))
        log.info("Engenheiro aprovou", decision=str(decision_path))
    else:
        console.print(
            "[yellow]Revisão: necessita correção. Rode[/yellow] forge dev run [yellow]após ajustes.[/yellow]"
        )
        log.warning("Engenheiro pediu correção", decision=str(decision_path))
