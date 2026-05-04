from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class WorkflowStep:
    INITIALIZED = "initialized"
    PLAN_READY = "plan_ready"
    PLAN_APPROVED = "plan_approved"
    DEV_DONE = "dev_done"
    QA_PASSED = "qa_passed"
    QA_FAILED = "qa_failed"
    REVIEWED_DONE = "reviewed_done"
    NEEDS_CORRECTION = "needs_correction"


@dataclass(frozen=True)
class ForgeState:
    phase: str
    step: str
    updated_at: str

    @staticmethod
    def initial() -> "ForgeState":
        return ForgeState(phase="mvp_v01", step=WorkflowStep.INITIALIZED, updated_at=_now_iso())

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict[str, str]) -> "ForgeState":
        phase = data.get("phase", "unknown")
        step = data.get("step", "unknown")
        # Migração Fase 0 -> Fase 1
        if phase == "phase0" and step == "initialized":
            phase = "mvp_v01"
        return ForgeState(
            phase=phase,
            step=step,
            updated_at=data.get("updated_at", _now_iso()),
        )
