"""Risk classification for terminal operations."""


class CommandPolicy:
    def classify(self, command):
        dangerous = ["rm -rf", "mkfs", "dd if=", "format"]
        if any(item in command for item in dangerous):
            return {"risk": "high", "confirmation": True}
        return {"risk": "low", "confirmation": False}
