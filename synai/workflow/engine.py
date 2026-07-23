"""Connect planning, execution, recovery, and reporting."""


class WorkflowEngine:
    def __init__(self, planner, executor, troubleshooter):
        self.planner = planner
        self.executor = executor
        self.troubleshooter = troubleshooter

    def run(self, request):
        plan = self.planner.plan(request)
        command = plan.get("command")
        if not command:
            return plan
        result = self.executor.run(command)
        if not result.get("success"):
            result["recovery"] = self.troubleshooter.analyze(result)
        return result
