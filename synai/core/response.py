"""Parse structured AI responses."""

from .actions import Action


def parse_response(data):
    return Action(
        action=data.get("action", "none"),
        command=data.get("command", ""),
        reason=data.get("reason", ""),
        risk=data.get("risk", "unknown"),
    )
