"""Structured messages exchanged between SYN-AI and AI backends."""

from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class AIMessage:
    action: str
    payload: Dict[str, Any]

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(action=data.get("action", "none"), payload=data)
