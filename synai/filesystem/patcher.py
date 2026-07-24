"""Apply generated file repairs."""


def apply_patch(original, replacement):
    """Return validated replacement content for a repaired file."""
    if not isinstance(replacement, str):
        raise TypeError("replacement must be a string")
    return replacement
