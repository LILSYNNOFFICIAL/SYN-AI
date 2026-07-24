"""Persistent command queue foundation."""

from collections import deque


class CommandQueue:
    def __init__(self):
        self.items = deque()

    def push(self, command):
        self.items.append(command)

    def pop(self):
        return self.items.popleft() if self.items else None

    def __len__(self):
        return len(self.items)
