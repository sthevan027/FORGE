from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import toml

from forge.core.forge_dir import ForgeDir


@dataclass(frozen=True)
class ForgeAIConfig:
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    api_key: str = ""
    ollama_base_url: str = "http://127.0.0.1:11434"

    def resolved_api_key(self) -> str:
        if self.api_key.strip():
            return self.api_key.strip()
        env_map = {
            "openai": "OPENAI_API_KEY",
            "claude": "ANTHROPIC_API_KEY",
            "ollama": "",  # optional for local
        }
        key = env_map.get(self.provider.lower(), "")
        if key:
            return os.environ.get(key, "").strip()
        return ""


DEFAULT_FORGE_TOML = """# Configuração de IA do Forge (pode sobrescrever com variáveis de ambiente)
[ai]
provider = "openai"  # openai | claude | ollama
model = "gpt-4o-mini"
api_key = ""
ollama_base_url = "http://127.0.0.1:11434"
"""


def load_ai_config(forge_dir: ForgeDir) -> ForgeAIConfig:
    path = forge_dir.config_file()
    if not path.exists():
        return ForgeAIConfig()
    data = toml.loads(path.read_text(encoding="utf-8"))
    section: dict[str, Any] = data.get("ai", {}) if isinstance(data, dict) else {}
    return ForgeAIConfig(
        provider=str(section.get("provider", "openai")),
        model=str(section.get("model", "gpt-4o-mini")),
        api_key=str(section.get("api_key", "")),
        ollama_base_url=str(section.get("ollama_base_url", "http://127.0.0.1:11434")),
    )


def ensure_default_config_file(forge_dir: ForgeDir, *, force: bool = False) -> Path:
    forge_dir.ensure_structure()
    path = forge_dir.config_file()
    if path.exists() and not force:
        return path
    path.write_text(DEFAULT_FORGE_TOML, encoding="utf-8")
    return path


def ensure_sample_briefing(forge_dir: ForgeDir) -> Path:
    forge_dir.ensure_structure()
    path = forge_dir.briefing_file()
    if path.exists():
        return path
    path.write_text(
        "# Briefing do projeto\n\n"
        "Descreva aqui o que você quer construir: objetivos, stack desejada, "
        "restrições e critérios de aceite.\n",
        encoding="utf-8",
    )
    return path
