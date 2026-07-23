"""Controlled file editing interface."""

from pathlib import Path


def write_file(path, content):
    Path(path).write_text(content)
