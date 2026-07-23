"""Safe command execution layer for Termux/Linux environments."""

from dataclasses import dataclass
import subprocess


@dataclass
class CommandResult:
    command: str
    output: str
    error: str
    return_code: int


class TerminalExecutor:
    """Runs shell commands and returns structured results."""

    def run(self, command: str) -> CommandResult:
        process = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True,
        )

        return CommandResult(
            command=command,
            output=process.stdout,
            error=process.stderr,
            return_code=process.returncode,
        )
