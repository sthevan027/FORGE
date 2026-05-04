from __future__ import annotations

from pathlib import Path

from forge.ai.adapter import AIAdapter
from forge.core.forge_dir import ForgeDir


_DEV_SYSTEM = """Você é o Dev Bot (fullstack provisório no MVP).
Com base no plano aprovado, gere uma entrega mínima coerente: pode ser pseudocódigo,
esboço de módulos, ou snippets em Markdown com blocos de código.
Organize em seções claras. Não invente APIs externas sem necessidade."""


class DevBot:
    def __init__(self, adapter: AIAdapter) -> None:
        self._adapter = adapter

    def run(self, forge_dir: ForgeDir, plan_text: str) -> str:
        user = (
            "Plano aprovado:\n\n"
            f"{plan_text.strip()}\n\n"
            "Produza a saída do desenvolvimento conforme as instruções do sistema."
        )
        return self._adapter.complete(_DEV_SYSTEM, user)

    def write_output(self, forge_dir: ForgeDir, content: str) -> Path:
        forge_dir.ensure_structure()
        path = forge_dir.dev_output_file()
        path.write_text(content.strip() + "\n", encoding="utf-8")
        return path
