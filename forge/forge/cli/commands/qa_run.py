from __future__ import annotations

import typer
from rich.console import Console

from forge.ai import factory as ai_factory
from forge.bots.qa import QABot
from forge.core.forge_dir import ForgeDir
from forge.core.logging import get_logger, setup_logging
from forge.state.machine import ForgeFlowError, ForgeStateMachine

qa_app = typer.Typer(help="Comandos do QA Bot (MVP).")


@qa_app.command("run")
def qa_run(
    path: str = typer.Option(".", "--path", "-p", help="Diretório do projeto."),
) -> None:
    setup_logging()
    log = get_logger()
    console = Console()
    forge_dir = ForgeDir.from_project_path(path)

    plan_path = forge_dir.plan_file()
    dev_path = forge_dir.dev_output_file()
    if not plan_path.exists():
        console.print("[red]Plano não encontrado.[/red]")
        raise typer.Exit(code=1)
    if not dev_path.exists():
        console.print("[red]Saída do Dev não encontrada. Rode:[/red] forge dev run")
        raise typer.Exit(code=1)

    plan_text = plan_path.read_text(encoding="utf-8")
    dev_text = dev_path.read_text(encoding="utf-8")

    try:
        adapter = ai_factory.get_adapter(forge_dir)
        qa_bot = QABot(adapter)
        result = qa_bot.run(forge_dir, plan_text, dev_text)
        qa_bot.write_report(forge_dir, result.report)
        machine = ForgeStateMachine(forge_dir)
        machine.after_qa_run(passed=result.passed)
    except ForgeFlowError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1)
    except Exception as exc:  # noqa: BLE001
        console.print(f"[red]Erro no QA Bot:[/red] {exc}")
        log.error("Erro no QA Bot", error=str(exc))
        raise typer.Exit(code=1)

    report_path = forge_dir.qa_report_file()
    if result.passed:
        console.print("[green]QA PASS — relatório em[/green]", str(report_path))
        log.info("QA passou", report=str(report_path))
    else:
        console.print("[red]QA FAIL — fluxo bloqueado até nova entrega (forge dev run).[/red]")
        console.print("Relatório:", str(report_path))
        log.warning("QA reprovou", report=str(report_path))
        raise typer.Exit(code=2)
