"""Command execution and output capture."""

import subprocess


class TerminalExecutor:
    def run(self, command):
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return {
            "command": command,
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "code": result.returncode,
        }
