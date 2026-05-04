from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ForgeDir:
    project_path: Path

    @property
    def path(self) -> Path:
        return self.project_path / ".forge"

    @staticmethod
    def from_project_path(path: str | Path) -> "ForgeDir":
        p = Path(path).expanduser().resolve()
        return ForgeDir(project_path=p)

    def ensure_structure(self) -> None:
        (self.path / "context").mkdir(parents=True, exist_ok=True)
        (self.path / "plans").mkdir(parents=True, exist_ok=True)
        (self.path / "tasks").mkdir(parents=True, exist_ok=True)
        (self.path / "qa").mkdir(parents=True, exist_ok=True)
        (self.path / "decisions").mkdir(parents=True, exist_ok=True)
        (self.path / "logs").mkdir(parents=True, exist_ok=True)
        (self.path / "config").mkdir(parents=True, exist_ok=True)

    def state_file(self) -> Path:
        return self.path / "state.json"

    def log_file(self) -> Path:
        return self.path / "logs" / "forge.log"

    def config_file(self) -> Path:
        return self.path / "config" / "forge.toml"

    def briefing_file(self) -> Path:
        return self.path / "context" / "briefing.md"

    def plan_file(self) -> Path:
        return self.path / "plans" / "plan.md"

    def dev_output_file(self) -> Path:
        return self.path / "tasks" / "dev_output.md"

    def qa_report_file(self) -> Path:
        return self.path / "qa" / "report.md"

    def engineer_decision_file(self) -> Path:
        return self.path / "decisions" / "engineer_review.md"

