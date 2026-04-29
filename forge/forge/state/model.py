from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class ForgeState:
    phase: str
    step: str
    updated_at: str

    @staticmethod
    def initial() -> "ForgeState":
        return ForgeState(phase="phase0", step="initialized", updated_at=_now_iso())

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict[str, str]) -> "ForgeState":
        return ForgeState(
            phase=data.get("phase", "unknown"),
            step=data.get("step", "unknown"),
            updated_at=data.get("updated_at", _now_iso()),
        )

