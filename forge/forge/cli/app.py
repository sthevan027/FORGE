from __future__ import annotations

import typer

from forge.cli.commands import approve as approve_cmd
from forge.cli.commands import dev_run as dev_cmd
from forge.cli.commands import engineer_review as engineer_cmd
from forge.cli.commands import init as init_cmd
from forge.cli.commands import logs as logs_cmd
from forge.cli.commands import plan as plan_cmd
from forge.cli.commands import qa_run as qa_cmd
from forge.cli.commands import status as status_cmd

app = typer.Typer(
    name="forge",
    help="Forge — orquestra workflow de engenharia assistida por IA.",
    no_args_is_help=True,
)

app.command(name="init")(init_cmd.run)
app.command(name="status")(status_cmd.show)
app.command(name="logs")(logs_cmd.show)
app.command(name="plan")(plan_cmd.run)

app.add_typer(approve_cmd.approve_app, name="approve")
app.add_typer(dev_cmd.dev_app, name="dev")
app.add_typer(qa_cmd.qa_app, name="qa")
app.add_typer(engineer_cmd.engineer_app, name="engineer")
