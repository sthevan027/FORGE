from __future__ import annotations

from dataclasses import replace

from forge.core.forge_dir import ForgeDir
from forge.core.logging import append_log_file
from forge.state.model import ForgeState, WorkflowStep, _now_iso
from forge.state.store import ForgeStateStore


class ForgeFlowError(RuntimeError):
    pass


class ForgeStateMachine:
    def __init__(self, forge_dir: ForgeDir) -> None:
        self._store = ForgeStateStore(forge_dir)
        self._forge_dir = forge_dir

    def _save(self, state: ForgeState) -> ForgeState:
        self._store.save(state)
        append_log_file(self._forge_dir, f"transition: phase={state.phase} step={state.step}")
        return state

    def _require_step(self, state: ForgeState, *allowed: str) -> None:
        if state.step not in allowed:
            allowed_txt = ", ".join(allowed)
            raise ForgeFlowError(
                f"Comando não permitido no estado atual ({state.step!r}). "
                f"Estados permitidos: {allowed_txt}"
            )

    def init(self, force: bool = False) -> ForgeState:
        if self._forge_dir.state_file().exists() and not force:
            state = self._store.load()
            append_log_file(self._forge_dir, "init: state já existe (use --force para recriar)")
            return state

        state = ForgeState.initial()
        self._store.save(state)
        append_log_file(self._forge_dir, "init: estado inicial criado")
        return state

    def after_plan(self) -> ForgeState:
        current = self._store.load()
        self._require_step(current, WorkflowStep.INITIALIZED)
        nxt = replace(current, step=WorkflowStep.PLAN_READY, updated_at=_now_iso())
        return self._save(nxt)

    def after_approve_plan(self) -> ForgeState:
        current = self._store.load()
        self._require_step(current, WorkflowStep.PLAN_READY)
        nxt = replace(current, step=WorkflowStep.PLAN_APPROVED, updated_at=_now_iso())
        return self._save(nxt)

    def after_dev_run(self) -> ForgeState:
        current = self._store.load()
        self._require_step(
            current,
            WorkflowStep.PLAN_APPROVED,
            WorkflowStep.NEEDS_CORRECTION,
            WorkflowStep.QA_FAILED,
        )
        nxt = replace(current, step=WorkflowStep.DEV_DONE, updated_at=_now_iso())
        return self._save(nxt)

    def after_qa_run(self, *, passed: bool) -> ForgeState:
        current = self._store.load()
        self._require_step(current, WorkflowStep.DEV_DONE)
        step = WorkflowStep.QA_PASSED if passed else WorkflowStep.QA_FAILED
        nxt = replace(current, step=step, updated_at=_now_iso())
        return self._save(nxt)

    def after_engineer_review(self, *, approved: bool) -> ForgeState:
        current = self._store.load()
        self._require_step(current, WorkflowStep.QA_PASSED)
        step = WorkflowStep.REVIEWED_DONE if approved else WorkflowStep.NEEDS_CORRECTION
        nxt = replace(current, step=step, updated_at=_now_iso())
        return self._save(nxt)

    # Compat: transição genérica legada (se ainda usada)
    def transition(self, *, phase: str | None = None, step: str | None = None) -> ForgeState:
        current = self._store.load()
        nxt = replace(
            current,
            phase=phase or current.phase,
            step=step or current.step,
            updated_at=_now_iso(),
        )
        return self._save(nxt)
