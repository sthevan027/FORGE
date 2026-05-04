from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from forge.ai.adapter import AIAdapter
from forge.core.forge_dir import ForgeDir


_QA_SYSTEM = """Você é o QA Bot. Avalie a entrega do desenvolvimento frente ao plano.
Responda em Markdown. A PRIMEIRA linha do relatório DEVE ser EXATAMENTE uma das opções:
VERDICT: PASS
ou
VERDICT: FAIL
Depois inclua seções ## Resumo, ## Achados, ## Riscos (se houver)."""


@dataclass(frozen=True)
class QAResult:
    passed: bool
    report: str


class QABot:
    def __init__(self, adapter: AIAdapter) -> None:
        self._adapter = adapter

    def run(self, forge_dir: ForgeDir, plan_text: str, dev_output: str) -> QAResult:
        user = (
            "Plano:\n\n"
            f"{plan_text.strip()}\n\n"
            "Entrega do Dev Bot:\n\n"
            f"{dev_output.strip()}\n"
        )
        report = self._adapter.complete(_QA_SYSTEM, user)
        passed = parse_qa_verdict(report)
        return QAResult(passed=passed, report=report)

    def write_report(self, forge_dir: ForgeDir, content: str) -> Path:
        forge_dir.ensure_structure()
        path = forge_dir.qa_report_file()
        path.write_text(content.strip() + "\n", encoding="utf-8")
        return path


def parse_qa_verdict(text: str) -> bool:
    for line in text.splitlines():
        line = line.strip()
        if re.match(r"(?i)^VERDICT:\s*PASS\s*$", line):
            return True
        if re.match(r"(?i)^VERDICT:\s*FAIL\s*$", line):
            return False
    lower = text.lower()
    if "verdict: fail" in lower:
        return False
    if "verdict: pass" in lower:
        return True
    return False
