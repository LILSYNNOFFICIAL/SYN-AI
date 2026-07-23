"""Verification stage for SYN-AI workflows.

Determines whether a completed action produced the expected result.
"""

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class VerificationResult:
    verified: bool
    message: str
    evidence: object = None


class WorkflowVerifier:
    """Validate workflow outcomes after execution."""

    def __init__(self, checker: Optional[Callable] = None):
        self.checker = checker

    def verify(self, result, expected=None):
        if self.checker:
            passed = self.checker(result, expected)
            return VerificationResult(
                verified=passed,
                message="Custom verification completed",
                evidence=result,
            )

        success = False
        if isinstance(result, dict):
            success = result.get("success", False)
        else:
            success = getattr(result, "success", False)

        return VerificationResult(
            verified=success,
            message="Execution state verification completed",
            evidence=result,
        )
