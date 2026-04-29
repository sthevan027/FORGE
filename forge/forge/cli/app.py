from __future__ import annotations

import typer

from forge.cli.commands import init as init_cmd
from forge.cli.commands import logs as logs_cmd
from forge.cli.commands import status as status_cmd

app = typer.Typer(
    name="forge",
    help="Forge — orquestra workflow de engenharia assistida por IA.",
    no_args_is_help=True,
)

app.command(name="init")(init_cmd.run)
app.command(name="status")(status_cmd.show)
app.command(name="logs")(logs_cmd.show)

