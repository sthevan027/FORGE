from __future__ import annotations

import typer

from forge.core.config import ensure_default_config_file, ensure_sample_briefing
from forge.core.forge_dir import ForgeDir
from forge.core.logging import get_logger, setup_logging
from forge.state.machine import ForgeStateMachine

app = typer.Typer(help="Inicializa a estrutura .forge/ no projeto atual.")


@app.command()
def run(
    path: str = typer.Option(".", "--path", "-p", help="Diretório alvo do projeto."),
    force: bool = typer.Option(False, "--force", help="Recria arquivos quando existirem."),
) -> None:
    setup_logging()
    log = get_logger()

    forge_dir = ForgeDir.from_project_path(path)
    forge_dir.ensure_structure()
    ensure_default_config_file(forge_dir, force=False)
    ensure_sample_briefing(forge_dir)
    state_machine = ForgeStateMachine(forge_dir)
    state_machine.init(force=force)

    log.info("Projeto inicializado", project_path=str(forge_dir.project_path), forge_path=str(forge_dir.path))

