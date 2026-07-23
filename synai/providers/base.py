"""AI provider interface."""


class Provider:
    def chat(self, message):
        raise NotImplementedError


class FreeProvider(Provider):
    def chat(self, message):
        return "Basic SYN-AI mode is ready. Connect an advanced provider for expanded reasoning."
