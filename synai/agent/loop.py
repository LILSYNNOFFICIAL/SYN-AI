"""Coordinate planning, execution, feedback, and recovery."""


class AgentLoop:
    def __init__(self, connector, safety, executor, feedback=None):
        self.connector = connector
        self.safety = safety
        self.executor = executor
        self.feedback = feedback

    def run(self, request):
        action = self.connector.send(request)
        if not self.safety.check(action.to_dict()):
            return {"success": False, "error": "blocked"}

        if self.feedback:
            return self.feedback.run(action.command)

        return self.executor.run(action.command)
