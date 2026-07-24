"""Lightweight persistent memory store for SYN-AI."""

import json
from pathlib import Path
from typing import Any, Dict


class MemoryStore:
    def __init__(self, path=".synai/memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data: Dict[str, Any] = self._load()

    def _load(self):
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self):
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key, default=None):
        return self.data.get(key, default)
