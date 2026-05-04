from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from forge.cli.app import app


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_workflow_happy_path_dry_run(tmp_path: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FORGE_DRY_RUN", "1")
    project = tmp_path / "proj"
    project.mkdir()

    r = runner.invoke(app, ["init", "--path", str(project)])
    assert r.exit_code == 0, r.stdout + r.stderr

    r = runner.invoke(app, ["plan", "--path", str(project)])
    assert r.exit_code == 0, r.stdout + r.stderr
    assert (project / ".forge" / "plans" / "plan.md").exists()

    r = runner.invoke(app, ["approve", "plan", "--path", str(project), "--yes"])
    assert r.exit_code == 0, r.stdout + r.stderr

    r = runner.invoke(app, ["dev", "run", "--path", str(project)])
    assert r.exit_code == 0, r.stdout + r.stderr
    assert (project / ".forge" / "tasks" / "dev_output.md").exists()

    r = runner.invoke(app, ["qa", "run", "--path", str(project)])
    assert r.exit_code == 0, r.stdout + r.stderr
    assert (project / ".forge" / "qa" / "report.md").exists()

    r = runner.invoke(app, ["engineer", "review", "--path", str(project)])
    assert r.exit_code == 0, r.stdout + r.stderr

    state = json.loads((project / ".forge" / "state.json").read_text(encoding="utf-8"))
    assert state["step"] == "reviewed_done"


def test_plan_wrong_state(tmp_path: Path, runner: CliRunner, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FORGE_DRY_RUN", "1")
    project = tmp_path / "p2"
    project.mkdir()
    runner.invoke(app, ["init", "--path", str(project)])
    runner.invoke(app, ["plan", "--path", str(project)])
    r = runner.invoke(app, ["plan", "--path", str(project)])
    assert r.exit_code == 1


def test_qa_fail_blocks_exit_code(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, runner: CliRunner) -> None:
    """Sem dry-run, usar adapter fake via env já definido — força QA FAIL com monkeypatch em factory."""

    project = tmp_path / "p3"
    project.mkdir()

    class FailQA:
        def complete(self, system: str, user: str) -> str:
            if "QA Bot" in system:
                return "VERDICT: FAIL\n\n## Resumo\nruim\n"
            if "Dev Bot" in system:
                return "out"
            if "DECISION:" in system:
                return "DECISION: approved\n"
            return "# Plano\n\n## Escopo\nx\n## Arquitetura\nx\n## Cronograma\nx\n"

    monkeypatch.setenv("FORGE_DRY_RUN", "0")

    import forge.ai.factory as factory

    monkeypatch.setattr(factory, "get_adapter", lambda _fd: FailQA())

    runner.invoke(app, ["init", "--path", str(project)])
    runner.invoke(app, ["plan", "--path", str(project)])
    runner.invoke(app, ["approve", "plan", "--path", str(project), "--yes"])
    runner.invoke(app, ["dev", "run", "--path", str(project)])
    r = runner.invoke(app, ["qa", "run", "--path", str(project)])
    assert r.exit_code == 2
    state = json.loads((project / ".forge" / "state.json").read_text(encoding="utf-8"))
    assert state["step"] == "qa_failed"
