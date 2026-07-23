"""Coordinate planning, execution, feedback, and recovery."""


class AgentLoop:
    def __init__(self, connector, safety, executor):
        self.connector = connector
        self.safety = safety
        self.executor = executor

    def run(self, request):
        action = self.connector.send(request)
        if not self.safety.check(action.to_dict()):
            return {"success": False, "error": "blocked"}
        return self.executor.run(action.command)
