"""Installation strategy engine for Termux/Linux."""

import shutil


class InstallationEngine:
    def choose_method(self, package):
        if shutil.which("pkg"):
            return {"method": "pkg", "command": f"pkg install {package} -y"}
        if shutil.which("apt"):
            return {"method": "apt", "command": f"apt install {package} -y"}
        if shutil.which("pip"):
            return {"method": "pip", "command": f"pip install {package}"}
        return {"method": "unknown", "command": None}

    def verify(self, command_result):
        return command_result.get("success", False)
