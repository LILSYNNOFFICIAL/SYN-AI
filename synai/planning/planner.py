"""SYN-AI natural language action planner.

Converts user objectives into executable workflow actions.
This is intentionally deterministic until an AI provider layer is connected.
"""

from dataclasses import dataclass


@dataclass
class PlannedAction:
    goal: str
    command: str
    reason: str


class ActionPlanner:
    """Create executable actions from user goals."""

    COMMAND_HINTS = {
        "install": "pkg install {target}",
        "update": "pkg update",
        "upgrade": "pkg upgrade",
    }

    def plan(self, request: str) -> dict:
        text = request.strip()
        lowered = text.lower()

        for keyword, template in self.COMMAND_HINTS.items():
            if keyword in lowered:
                target = self._extract_target(text, keyword)
                return PlannedAction(
                    goal=text,
                    command=template.format(target=target),
                    reason=f"Detected {keyword} request",
                ).__dict__

        return PlannedAction(
            goal=text,
            command=text,
            reason="No transformation available, passing request for execution layer",
        ).__dict__

    def _extract_target(self, text: str, keyword: str) -> str:
        parts = text.lower().split(keyword, 1)
        if len(parts) == 2 and parts[1].strip():
            return parts[1].strip()
        return ""
