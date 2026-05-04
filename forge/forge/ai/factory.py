from __future__ import annotations

import os

from forge.ai.adapter import AIAdapter
from forge.ai.claude_adapter import ClaudeAdapter
from forge.ai.ollama_adapter import OllamaAdapter
from forge.ai.openai_adapter import OpenAIAdapter
from forge.core.config import ForgeAIConfig, load_ai_config
from forge.core.forge_dir import ForgeDir


class DryRunAdapter:
    """Adapter determinístico para testes (FORGE_DRY_RUN=1)."""

    def complete(self, system: str, user: str) -> str:
        if "QA Bot" in system or "VERDICT" in system:
            return (
                "VERDICT: PASS\n\n"
                "## Resumo\n"
                "Checklist básico atendido (dry-run).\n"
            )
        if "DECISION:" in system and "revisão" in system.lower():
            return "DECISION: approved\n\nResumo: aprovado em dry-run."
        if "Dev Bot" in system:
            return (
                "# Saída do Dev (dry-run)\n\n"
                "```python\nprint('forge-dry-run')\n```\n"
            )
        return (
            "# Plano (dry-run)\n\n"
            "## Escopo\n"
            "MVP de exemplo.\n\n"
            "## Arquitetura\n"
            "CLI + módulos Python.\n\n"
            "## Cronograma\n"
            "- Semana 1: base\n"
        )


def get_adapter(forge_dir: ForgeDir) -> AIAdapter:
    if os.environ.get("FORGE_DRY_RUN", "").strip() in {"1", "true", "yes"}:
        return DryRunAdapter()

    cfg = load_ai_config(forge_dir)
    provider = cfg.provider.lower().strip()
    if provider == "openai":
        key = cfg.resolved_api_key()
        if not key:
            msg = "Configure OPENAI_API_KEY ou [ai].api_key em .forge/config/forge.toml"
            raise RuntimeError(msg)
        return OpenAIAdapter(api_key=key, model=cfg.model)
    if provider in {"claude", "anthropic"}:
        key = cfg.resolved_api_key()
        if not key:
            msg = "Configure ANTHROPIC_API_KEY ou [ai].api_key em .forge/config/forge.toml"
            raise RuntimeError(msg)
        return ClaudeAdapter(api_key=key, model=cfg.model)
    if provider == "ollama":
        return OllamaAdapter(base_url=cfg.ollama_base_url, model=cfg.model)
    raise RuntimeError(f"Provedor de IA desconhecido: {cfg.provider!r}")
