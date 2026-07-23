"""Natural language intent planner."""


class IntentPlanner:
    def plan(self, request):
        text = request.lower()

        if "update" in text and "everything" in text:
            return {"intent": "system_update", "command": "pkg update && pkg upgrade -y"}

        if text.startswith("install "):
            package = request[8:].strip()
            return {"intent": "install", "command": f"pkg install {package} -y"}

        return {"intent": "unknown", "message": "No command plan available yet."}
