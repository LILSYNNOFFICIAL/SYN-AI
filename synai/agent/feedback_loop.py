"""SYN-AI execution feedback loop.

Connects command execution results with repair decisions.
"""

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class ExecutionCycle:
    command: str
    success: bool
    output: str
    attempts: int = 1


class FeedbackLoop:
    """Coordinates execute -> analyze -> repair -> retry workflows."""

    def __init__(self, executor: Callable, analyzer: Callable, fixer: Callable):
        self.executor = executor
        self.analyzer = analyzer
        self.fixer = fixer

    def run(self, command: str, max_retries: int = 3) -> ExecutionCycle:
        attempts = 0
        current_command = command

        while attempts < max_retries:
            attempts += 1
            result = self.executor(current_command)

            if result.success:
                return ExecutionCycle(
                    command=current_command,
                    success=True,
                    output=result.output,
                    attempts=attempts,
                )

            failure_context = self.analyzer(result)
            repair = self.fixer(failure_context)

            if not repair:
                break

            current_command = repair

        return ExecutionCycle(
            command=current_command,
            success=False,
            output="Execution failed after repair attempts",
            attempts=attempts,
        )
