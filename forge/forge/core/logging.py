from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.logging import RichHandler

from forge.core.forge_dir import ForgeDir

_LOGGER_NAME = "forge"


def setup_logging(level: int = logging.INFO) -> None:
    logger = logging.getLogger(_LOGGER_NAME)
    logger.setLevel(level)

    if any(isinstance(h, RichHandler) for h in logger.handlers):
        return

    handler = RichHandler(rich_tracebacks=True, show_time=False, show_path=False)
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def get_logger() -> "ForgeLogger":
    return ForgeLogger(logging.getLogger(_LOGGER_NAME))


class ForgeLogger:
    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def info(self, message: str, **context: Any) -> None:
        self._logger.info(_format(message, context))

    def warning(self, message: str, **context: Any) -> None:
        self._logger.warning(_format(message, context))

    def error(self, message: str, **context: Any) -> None:
        self._logger.error(_format(message, context))


def _format(message: str, context: dict[str, Any]) -> str:
    if not context:
        return message
    suffix = " ".join(f"{k}={_safe(v)}" for k, v in context.items())
    return f"{message}  {suffix}"


def _safe(value: Any) -> str:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return str(value)
    return repr(value)


def append_log_file(forge_dir: ForgeDir, line: str) -> None:
    forge_dir.ensure_structure()
    path = forge_dir.log_file()
    timestamp = datetime.now(timezone.utc).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8") if not path.exists() else None
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp} {line}\n")


def read_log_file(forge_dir: ForgeDir, tail: int = 200) -> list[str]:
    path = forge_dir.log_file()
    if not path.exists():
        return []

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    if tail <= 0:
        return lines
    return lines[-tail:]

