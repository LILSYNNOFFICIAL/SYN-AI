"""Environment discovery for Termux/Linux systems."""

import os
import platform
import shutil
import subprocess
import sys


class EnvironmentScanner:
    def scan(self):
        return {
            "platform": platform.platform(),
            "architecture": platform.machine(),
            "python": sys.version,
            "termux": os.path.exists("/data/data/com.termux"),
            "storage": shutil.disk_usage("/")._asdict(),
            "tools": self._tools(["pkg", "apt", "pip", "git"]),
        }

    def _tools(self, names):
        return {name: shutil.which(name) is not None for name in names}
