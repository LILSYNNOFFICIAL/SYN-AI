"""Safe file reading interface."""

from pathlib import Path


def read_file(path):
    return Path(path).read_text()
