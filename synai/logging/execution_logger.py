"""Execution history tracking for SYN-AI tasks."""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


class ExecutionLogger:
    def __init__(self, path=".synai/history.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> List[Dict[str, Any]]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def record(self, task_id: str, state: str, details=None):
        history = self._load()
        history.append({
            "task_id": task_id,
            "state": state,
            "details": details or {},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        self.path.write_text(json.dumps(history, indent=2), encoding="utf-8")

    def all(self):
        return self._load()
