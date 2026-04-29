from __future__ import annotations

from dataclasses import replace

from forge.core.forge_dir import ForgeDir
from forge.core.logging import append_log_file
from forge.state.model import ForgeState, _now_iso
from forge.state.store import ForgeStateStore


class ForgeStateMachine:
    def __init__(self, forge_dir: ForgeDir) -> None:
        self._store = ForgeStateStore(forge_dir)
        self._forge_dir = forge_dir

    def init(self, force: bool = False) -> ForgeState:
        if self._forge_dir.state_file().exists() and not force:
            state = self._store.load()
            append_log_file(self._forge_dir, "init: state já existe (use --force para recriar)")
            return state

        state = ForgeState.initial()
        self._store.save(state)
        append_log_file(self._forge_dir, "init: estado inicial criado")
        return state

    def transition(self, *, phase: str | None = None, step: str | None = None) -> ForgeState:
        current = self._store.load()
        next_state = replace(
            current,
            phase=phase or current.phase,
            step=step or current.step,
            updated_at=_now_iso(),
        )
        self._store.save(next_state)
        append_log_file(self._forge_dir, f"transition: phase={next_state.phase} step={next_state.step}")
        return next_state

