"""Command execution and output capture."""

import subprocess

from .output import normalize


class TerminalExecutor:
    """Execute commands and return normalized SYN-AI results."""

    def __init__(self, timeout=60):
        self.timeout = timeout

    def run(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True,
                timeout=self.timeout,
            )
            return normalize(
                stdout=result.stdout,
                stderr=result.stderr,
                code=result.returncode,
            )
        except subprocess.TimeoutExpired as error:
            return normalize(
                stdout="",
                stderr=str(error),
                code=124,
            )
