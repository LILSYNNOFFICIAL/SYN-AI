"""Core SYN-AI agent loop."""

from synai.terminal.executor import TerminalExecutor


class SYNAgent:
    def __init__(self):
        self.terminal = TerminalExecutor()

    def execute_task(self, command: str):
        """Execute an approved command generated from an AI plan."""
        return self.terminal.run(command)
