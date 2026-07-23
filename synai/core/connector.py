"""Bridge between reasoning backend and local SYN-AI executor."""

from .response import parse_response


class AIConnector:
    def __init__(self, backend=None):
        self.backend = backend

    def send(self, request):
        if not self.backend:
            raise RuntimeError("AI backend not configured")
        return parse_response(self.backend(request))
