"""Persistent workflow state foundation."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class WorkflowState:
    task_id: str
    retries: int = 0
    completed: bool = False
    history: List[str] = field(default_factory=list)
    repairs: Dict[str, str] = field(default_factory=dict)


class StateStore:
    """In-memory state store foundation for future persistence."""

    def __init__(self):
        self.states = {}

    def save(self, state):
        self.states[state.task_id] = state

    def load(self, task_id):
        return self.states.get(task_id)
