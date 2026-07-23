"""Failure to repair action translation foundation."""

from dataclasses import dataclass


@dataclass
class RepairAction:
    action_type: str
    command: str
    reason: str


class RepairEngine:
    """Convert known failures into recovery actions."""

    def create_action(self, failure):
        if not failure:
            return None

        text = str(failure).lower()

        if "modulenotfounderror" in text:
            package = text.split("modulenotfounderror")[-1].strip(" :'")
            return {
                "command": f"pip install {package}",
                "reason": "Install missing Python dependency",
            }

        if "permission denied" in text:
            return {
                "command": "chmod +x",
                "reason": "Repair executable permission issue",
            }

        return None
