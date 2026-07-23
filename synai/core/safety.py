"""Command safety controls for SYN-AI execution."""

from dataclasses import dataclass


@dataclass
class SafetyDecision:
    allowed: bool
    risk: str
    reason: str


class CommandSafety:
    """Basic command risk classifier before execution."""

    HIGH_RISK = (
        "rm -rf",
        "mkfs",
        "dd if=",
        "format",
        "shutdown",
    )

    def evaluate(self, action):
        command = action.get("command", "") if isinstance(action, dict) else str(action)

        for pattern in self.HIGH_RISK:
            if pattern in command:
                return SafetyDecision(
                    allowed=False,
                    risk="high",
                    reason=f"Blocked dangerous command pattern: {pattern}",
                )

        return SafetyDecision(
            allowed=True,
            risk="normal",
            reason="Command passed safety checks",
        )

    def check(self, action):
        return self.evaluate(action).allowed
