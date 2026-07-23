"""Failure analysis foundation for SYN-AI."""

from dataclasses import dataclass


@dataclass
class FailureContext:
    message: str
    category: str
    suggestions: list


class Troubleshooter:
    """Convert execution failures into structured repair context."""

    RULES = {
        "not found": "missing_dependency",
        "permission denied": "permission_issue",
        "syntax error": "code_error",
        "no such file": "missing_file",
    }

    def analyze(self, output):
        text = str(output).lower()

        for pattern, category in self.RULES.items():
            if pattern in text:
                return FailureContext(
                    message=output,
                    category=category,
                    suggestions=[],
                )

        return FailureContext(
            message=output,
            category="unknown",
            suggestions=[],
        )
