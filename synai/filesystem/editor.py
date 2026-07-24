"""Controlled file editing interface."""

from pathlib import Path


def write_file(path, content):
    """Write UTF-8 content and create missing directories."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return target
