"""Environment detection foundation for SYN-AI runtime."""

import platform
import sys
from dataclasses import dataclass


@dataclass
class EnvironmentInfo:
    platform: str
    distro: str
    package_manager: str
    python_version: str


class EnvironmentDetector:
    """Detect host environment and available package manager."""

    def detect(self):
        system = platform.system().lower()

        if "android" in system or self._is_termux():
            return EnvironmentInfo(
                platform="android",
                distro="termux",
                package_manager="pkg",
                python_version=sys.version.split()[0],
            )

        package_manager = self._detect_package_manager()

        return EnvironmentInfo(
            platform=system,
            distro=self._detect_distro(),
            package_manager=package_manager,
            python_version=sys.version.split()[0],
        )

    def _is_termux(self):
        return "TERMUX_VERSION" in __import__("os").environ

    def _detect_distro(self):
        try:
            import distro
            return distro.id()
        except ImportError:
            return platform.platform()

    def _detect_package_manager(self):
        import shutil

        for manager in ("apt", "pacman", "dnf", "yum", "apk"):
            if shutil.which(manager):
                return manager
        return "unknown"
