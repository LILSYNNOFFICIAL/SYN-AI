"""Task lifecycle states used by SYN-AI."""

from enum import Enum


class TaskState(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    REPAIRED = "repaired"
