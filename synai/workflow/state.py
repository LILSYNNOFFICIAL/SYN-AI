"""Persistent workflow state foundation."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class WorkflowState:
    task_id: str
    retries: int = 0
    completed: bool = False
    history: List[str] = field(default_factory=list)
    repairs: Dict[str, str] = field(default_factory=dict)

    def record(self, event: str):
        self.history.append(event)

    def add_retry(self):
        self.retries += 1
        self.record(f"retry:{self.retries}")

    def mark_complete(self):
        self.completed = True
        self.record("completed")


class StateStore:
    """In-memory state store foundation for future persistence."""

    def __init__(self):
        self.states = {}

    def save(self, state: WorkflowState):
        self.states[state.task_id] = state

    def load(self, task_id: str) -> Optional[WorkflowState]:
        return self.states.get(task_id)
