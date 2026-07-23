"""Environment detection foundation for SYN-AI runtime."""

import platform
import shutil
import sys
from dataclasses import dataclass, field


@dataclass
class EnvironmentInfo:
    platform: str
    distro: str
    package_manager: str
    python_version: str
    installed_tools: list = field(default_factory=list)


class EnvironmentDetector:
    """Detect host environment, package manager, and available tools."""

    def detect(self):
        system = platform.system().lower()

        if "android" in system or self._is_termux():
            info = EnvironmentInfo(
                platform="android",
                distro="termux",
                package_manager="pkg",
                python_version=sys.version.split()[0],
            )
        else:
            info = EnvironmentInfo(
                platform=system,
                distro=self._detect_distro(),
                package_manager=self._detect_package_manager(),
                python_version=sys.version.split()[0],
            )

        info.installed_tools = self._detect_tools()
        return info

    def _is_termux(self):
        return "TERMUX_VERSION" in __import__("os").environ

    def _detect_distro(self):
        try:
            import distro
            return distro.id()
        except ImportError:
            return platform.platform()

    def _detect_package_manager(self):
        for manager in ("apt", "pacman", "dnf", "yum", "apk"):
            if shutil.which(manager):
                return manager
        return "unknown"

    def _detect_tools(self):
        return [
            tool
            for tool in ("python", "pip", "git", "curl", "nmap")
            if shutil.which(tool)
        ]
