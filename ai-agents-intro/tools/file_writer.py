#!/usr/bin/env python3
"""
Deterministic tool for saving Markdown content to disk
"""
from pathlib import Path


def save_markdown_file(file_path: str, content: str) -> str:
    """Writes Markdown content to file_path, creating parent directories
    as needed, and returns the saved path"""
    path = Path(file_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except OSError as error:
        raise OSError(f"Could not save '{file_path}': {error}") from error
    return str(path)
