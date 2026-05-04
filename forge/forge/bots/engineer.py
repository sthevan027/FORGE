from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from forge.ai.adapter import AIAdapter
from forge.core.forge_dir import ForgeDir


_PLAN_SYSTEM = """Você é um Engenheiro de Software sênior coordenando um time de IAs.
Gere um plano técnico em Markdown com seções obrigatórias:
## Escopo
## Arquitetura
## Cronograma
Seja objetivo e alinhado ao briefing do usuário."""

_REVIEW_SYSTEM = """Você é o Engenheiro responsável pela revisão final.
Com base no relatório de QA e no contexto do projeto, decida o próximo passo.
Responda em texto simples com a PRIMEIRA linha EXATAMENTE no formato:
DECISION: approved
ou
DECISION: needs_correction
Depois, explique brevemente o motivo."""


@dataclass(frozen=True)
class EngineerReviewResult:
    approved: bool
    raw: str


class EngineerBot:
    def __init__(self, adapter: AIAdapter) -> None:
        self._adapter = adapter

    def generate_plan(self, forge_dir: ForgeDir, briefing_text: str) -> str:
        user = (
            "Briefing do projeto:\n\n"
            f"{briefing_text}\n\n"
            "Produza o plano completo em Markdown."
        )
        return self._adapter.complete(_PLAN_SYSTEM, user)

    def write_plan(self, forge_dir: ForgeDir, content: str) -> Path:
        forge_dir.ensure_structure()
        path = forge_dir.plan_file()
        path.write_text(content.strip() + "\n", encoding="utf-8")
        return path

    def review(self, forge_dir: ForgeDir, qa_report: str, extra_context: str = "") -> EngineerReviewResult:
        user = (
            "Relatório de QA:\n\n"
            f"{qa_report.strip()}\n\n"
        )
        if extra_context.strip():
            user += f"Contexto adicional:\n\n{extra_context.strip()}\n\n"
        user += "Emita a decisão conforme o formato pedido."
        raw = self._adapter.complete(_REVIEW_SYSTEM, user)
        approved = _parse_engineer_decision(raw)
        return EngineerReviewResult(approved=approved, raw=raw)

    def write_decision(self, forge_dir: ForgeDir, content: str) -> Path:
        forge_dir.ensure_structure()
        path = forge_dir.engineer_decision_file()
        path.write_text(content.strip() + "\n", encoding="utf-8")
        return path


def _parse_engineer_decision(text: str) -> bool:
    for line in text.splitlines():
        line = line.strip()
        if re.match(r"(?i)^DECISION:\s*approved\s*$", line):
            return True
        if re.match(r"(?i)^DECISION:\s*needs_correction\s*$", line):
            return False
    # fallback: palavras-chave
    lower = text.lower()
    if "needs_correction" in lower:
        return False
    if "approved" in lower:
        return True
    return False
