"""SYN-AI environment awareness layer.

Collects runtime context before planning so workflow decisions can adapt
to the actual machine running SYN-AI.
"""

import platform
import shutil


class EnvironmentContext:
    """Detect local execution environment details."""

    def collect(self) -> dict:
        return {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": platform.python_version(),
            "available_tools": self._tools(),
        }

    def _tools(self) -> list[str]:
        tools = ["pkg", "apt", "pip", "git"]
        return [tool for tool in tools if shutil.which(tool)]
