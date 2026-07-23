"""Normalize terminal execution results."""


def normalize(stdout="", stderr="", code=0):
    return {
        "stdout": stdout,
        "stderr": stderr,
        "exit_code": code,
        "success": code == 0,
    }
