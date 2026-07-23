"""High-level SYN-AI operator loop."""


class SynOperator:
    def __init__(self, planner, runtime):
        self.planner = planner
        self.runtime = runtime

    def handle_request(self, request: str):
        action = self.planner.plan(request)
        return self.runtime.execute(action)
