"""High-level SYN-AI operator loop."""


class SynOperator:
    def __init__(self, planner, runtime, environment=None):
        self.planner = planner
        self.runtime = runtime
        self.environment = environment

    def handle_request(self, request: str):
        context = None
        if self.environment:
            context = self.environment.collect()

        action = self.planner.plan(request, context=context)
        return self.runtime.execute(action)
