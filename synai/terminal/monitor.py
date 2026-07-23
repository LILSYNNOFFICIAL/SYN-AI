"""Capture command execution results."""

from .output import normalize


class TerminalMonitor:
    def capture(self, process):
        return normalize(process.stdout, process.stderr, process.returncode)
