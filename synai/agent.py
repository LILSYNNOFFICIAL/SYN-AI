"""Core SYN-AI agent planner."""

from synai.terminal.executor import TerminalExecutor
from synai.planner.intent import IntentPlanner


class SYNAgent:
    def __init__(self):
        self.executor = TerminalExecutor()
        self.planner = IntentPlanner()

    def handle(self, request):
        action = self.planner.plan(request)
        if action.get("command"):
            return self.executor.run(action["command"])
        return action
