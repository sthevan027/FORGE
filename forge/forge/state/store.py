from __future__ import annotations

import json

from forge.core.forge_dir import ForgeDir
from forge.state.model import ForgeState


class ForgeStateStore:
    def __init__(self, forge_dir: ForgeDir) -> None:
        self._forge_dir = forge_dir

    def load(self) -> ForgeState:
        path = self._forge_dir.state_file()
        if not path.exists():
            return ForgeState.initial()
        data = json.loads(path.read_text(encoding="utf-8"))
        return ForgeState.from_dict(data)

    def save(self, state: ForgeState) -> None:
        self._forge_dir.ensure_structure()
        path = self._forge_dir.state_file()
        path.write_text(json.dumps(state.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

