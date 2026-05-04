from __future__ import annotations

import httpx


class OllamaAdapter:
    def __init__(self, *, base_url: str, model: str) -> None:
        self._base = base_url.rstrip("/")
        self._model = model

    def complete(self, system: str, user: str) -> str:
        url = f"{self._base}/api/chat"
        payload = {
            "model": self._model,
            "stream": False,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
        with httpx.Client(timeout=120.0) as client:
            response = client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
        msg = data.get("message") or {}
        content = msg.get("content", "")
        return str(content).strip()
