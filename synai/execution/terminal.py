"""SYN-AI terminal execution engine.

Provides the runtime layer that allows SYN-AI to execute commands and
return structured results to the agent workflow.
"""

import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class CommandResult:
    success: bool
    command: str
    output: str
    error: str
    exit_code: int


class TerminalExecutor:
    """Execute terminal commands and capture results."""

    def __init__(self, timeout: Optional[int] = 300):
        self.timeout = timeout

    def run(self, command: str) -> dict:
        try:
            process = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )

            result = CommandResult(
                success=process.returncode == 0,
                command=command,
                output=process.stdout,
                error=process.stderr,
                exit_code=process.returncode,
            )

            return result.__dict__

        except subprocess.TimeoutExpired as exc:
            return CommandResult(
                success=False,
                command=command,
                output="",
                error=f"Command timed out: {exc}",
                exit_code=-1,
            ).__dict__
