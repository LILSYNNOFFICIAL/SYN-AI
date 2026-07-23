"""SYN-AI runtime coordinator.

Connects planning components into an execution, recovery, and verification pipeline.
"""

from dataclasses import dataclass


@dataclass
class WorkflowResult:
    success: bool
    stage: str
    result: object


class WorkflowRuntime:
    """Coordinate safety, execution, recovery, and verification components."""

    def __init__(self, safety, executor, troubleshooter=None, feedback=None, verifier=None, repair=None):
        self.safety = safety
        self.executor = executor
        self.troubleshooter = troubleshooter
        self.feedback = feedback
        self.verifier = verifier
        self.repair = repair

    def execute(self, action):
        if not self.safety.check(action):
            return WorkflowResult(False, "safety", "Action blocked")

        result = self.executor.run(action["command"])

        if not result.get("success", False):
            analysis = None
            if self.troubleshooter:
                analysis = self.troubleshooter.analyze(result)

            if self.repair:
                repaired = self.repair.create_action(analysis)
                if repaired:
                    retry = self.execute(repaired)
                    if retry.success:
                        return retry

            return WorkflowResult(False, "analysis", analysis)

        if self.verifier:
            verification = self.verifier.verify(result, action)
            return WorkflowResult(
                verification.verified,
                "verify",
                verification,
            )

        return WorkflowResult(True, "complete", result)
