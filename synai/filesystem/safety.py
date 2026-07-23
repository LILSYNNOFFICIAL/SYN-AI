"""Filesystem safety primitives for SYN-AI edits."""

from dataclasses import dataclass


@dataclass
class FileChange:
    path: str
    before: str
    after: str


class FileSafety:
    """Provides validation points before filesystem mutation."""

    def preview(self, path: str, before: str, after: str) -> FileChange:
        return FileChange(path=path, before=before, after=after)

    def validate(self, change: FileChange) -> bool:
        return bool(change.path and change.after is not None)

    def backup_required(self, change: FileChange) -> bool:
        return change.before != change.after
